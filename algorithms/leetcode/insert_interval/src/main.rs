impl Solution {
    pub fn insert(intervals: Vec<Vec<i32>>, new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        Vec<Vec<i32>> res = []

        for i in 0..intervals.len() {
            if new_interval[1] < intervals[i][0] {
                intervals.insert(i, new_interval);
                break;
            } elseif intervals[i][0] > intervals[i][1] {
                intervals.insert()
            }
        }

        res
    }
}
