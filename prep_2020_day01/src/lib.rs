pub fn part1 () -> i64 {

    let nums = get_puzzle_input();

    for num in &nums {
        let remainder = 2020 - num;

        if nums.contains(&remainder) {
            return num * remainder
        }
    }
    0
}


pub fn part2 () -> i64 {

    let nums = get_puzzle_input();

    for num1 in &nums {
        for num2 in &nums {
            let remainder = 2020 - num1 - num2;

            if nums.contains(&remainder) {
                return num1 * num2 * remainder
            }
        }
    }
    0
}

pub fn get_puzzle_input() -> Vec<i64> {
    std::fs::read_to_string(String::from("input.txt")).expect("Failed to open file")
        .lines()
        .map(|line| line.parse().expect("Failed to parse line to i64"))
        .collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn part1_works() {
	
        let rust_answer = part1();
        let python_answer = 751776;

        assert_eq!(rust_answer, python_answer);
    }

    #[test]
    fn part2_works() {

        let rust_answer = part2();
        let python_answer = 42275090;

        assert_eq!(rust_answer, python_answer);
    }
}
