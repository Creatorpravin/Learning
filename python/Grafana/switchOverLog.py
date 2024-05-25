#!/usr/bin/env python3
import sys
sys.path.append('/home/chiefnet/.local/lib/python3.8/site-packages')
import urllib.request
from confluent_kafka.admin import AdminClient
import json
import re
from datetime import datetime
import os

SWITCHOVER_LOG_FILE_PATH = "/home/chiefnet/ChiefNet/CPE/LogFiles/SwitchOver.log"
LAST_SYCN_FILE_PATH = '/etc/telegraf/custom_scripts/LastSyncTime.txt'
SWITCHOVER_JSON_FILE_PATH = '/etc/telegraf/custom_scripts/SwitchOver.json'

# Function to read the last sync time from a file
def read_last_sync_time(sync_file_path):
    try:
        with open(sync_file_path, 'r') as sync_file:
            last_sync_time = sync_file.readline().strip()
            if last_sync_time:
                return datetime.fromisoformat(last_sync_time)
            else:
                return None
    except FileNotFoundError:
        return None

# Function to write the last sync time to a file
def write_last_sync_time(sync_file_path, last_sync_time):
    with open(sync_file_path, 'w') as sync_file:
        sync_file.write(last_sync_time.isoformat())

# Function to parse a log line
def parse_log_line(line):
    log_pattern = re.compile(
        r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) \| '
        r'(?P<level>\w+) \| '
        r'(?P<file_name>\w+\.py) \| '
        r'(?P<line_number>\d+) \| '
        r'(?P<module_name>\w+) \| '
        r'(?P<function_name>\w+) \| '
        r'(?P<config>.+) \((?P<interface>\w+)\) is applied on (?P<config_name>.+) \((?P<config_number>\d+)\) configuration'
    )
    match = log_pattern.match(line)
    if match:
        log_data = match.groupdict()
        return {
            'interface': log_data['interface'],
            'Configuration': log_data['config'],
            'Configuration Number': log_data['config_number'],
            'Configuration Name': log_data['config_name'],
            'Timestamp': log_data['timestamp']
        }
    else:
        return None

# Function to convert log entries from a specific time to JSON
def convert_log_to_json_from_time(log_file_path, json_file_path, sync_file_path):
    last_sync_time = read_last_sync_time(sync_file_path)
    latest_timestamp = None
    log_entries = []
    if os.path.isfile(log_file_path):
        with open(log_file_path, 'r') as log_file:
            for line in log_file:
                parsed_line = parse_log_line(line)
                if parsed_line:
                    # Convert timestamp string to datetime object
                    timestamp = datetime.strptime(parsed_line['Timestamp'], '%Y-%m-%d %H:%M:%S,%f')
                    
                    # Update latest_timestamp
                    if latest_timestamp is None or timestamp > latest_timestamp:
                        latest_timestamp = timestamp
                    
                    # Process only entries after the last sync time
                    if last_sync_time is None or timestamp > last_sync_time:
                        parsed_line['Timestamp'] = timestamp.isoformat()
                        log_entries.append(parsed_line)
    else:
        print(log_entries)
        return None
    
    if log_entries:
        print(log_entries)
        with open(json_file_path, 'w') as json_file:
            json.dump(log_entries, json_file, indent=4)
        
        # Update the last sync time file
        write_last_sync_time(sync_file_path, latest_timestamp)


def influx_health_check(url):
    try:
        response = urllib.request.urlopen(url + "/health")
        data = json.loads((response.read()).decode("utf-8"))

        if data["status"] == "pass":
            return True
    except Exception as e:
        return False

def kafka_health_check(kafka_broker):
    try:
        admin_client = AdminClient(kafka_broker)
        topics = admin_client.list_topics(timeout=5).topics
        if topics:
            return True
        else:
            return False
    except Exception as e:
        return False



influx_URL = "http://chiefnet-stg.influx.yavar.in"
kafka_broker = {
    'bootstrap.servers': 'chiefnet-stg.kafka.yavar.in:9092',
    'security.protocol': 'SASL_SSL', 
    'sasl.mechanism': 'SCRAM-SHA-512',
    'sasl.username': 'admin',
    'sasl.password': 'Yavar@123$',
    'enable.ssl.certificate.verification': False
}

if influx_health_check(influx_URL) & kafka_health_check(kafka_broker):
    convert_log_to_json_from_time(log_file_path=SWITCHOVER_LOG_FILE_PATH, json_file_path=SWITCHOVER_JSON_FILE_PATH, sync_file_path=LAST_SYCN_FILE_PATH)