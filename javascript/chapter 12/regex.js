const string = 'black*raven lime*parrot white*seagull';
const regex = /(?<color>.*?)\*(?<bird>[a-z0-9]+)/g;
while (match = regex.exec(string))
{
    let value = match[0];
    let index = match.index;
    let input = match.input;
    console.log(`${value} at ${index} with '${input}`);
    console.log(match.groups.color);
    console.log(match.groups.bird);

}