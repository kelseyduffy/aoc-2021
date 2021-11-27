pub fn part1 (contents: &str) -> i64 {

    0
}


pub fn part2 (contents: &str) -> i64 {

    0
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::fs;

    #[test]
    fn part1_works() {
        let filename = String::from("input.txt");
        let contents = fs::read_to_string(filename)
            .expect("Failed to open file");
	
        let rust_answer = part1(&contents);
        let python_answer = 751776;

        assert_eq!(rust_answer, python_answer);
    }

    #[test]
    fn part2_works() {
        let filename = String::from("input.txt");
        let contents = fs::read_to_string(filename)
            .expect("Failed to open file");

        let rust_answer = part2(&contents);
        let python_answer = 42275090;

        assert_eq!(rust_answer, python_answer);
    }
}
