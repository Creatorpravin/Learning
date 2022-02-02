function sumIntervals(intervals) {
    let arr = [];
    for (let i = 0; i < intervals.length; i++) {
      arr.push(
        Array.from(
          { length: intervals[i][1] - intervals[i][0] },
          (x, j) => j + 1 + intervals[i][0]
        )
      );
    }
    return [...new Set([].concat(...arr))].length;
  }