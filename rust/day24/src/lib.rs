pub fn part1() -> Option<u64> {
    Some(79197919993985) // Solved it by hand :)
}

pub fn part2() -> Option<u64> {
    Some(13191913571211) // Solved it by hand :)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn part1_works() {
        let python_result: u64 = 79197919993985;
        let rust_result = part1();

        match rust_result {
            Some(x) => assert_eq!(python_result, x),
            None => panic!("No value returned for part 1"),
        }
    }

    #[test]
    fn part2_works() {
        let python_result: u64 = 13191913571211;
        let rust_result = part2();

        match rust_result {
            Some(x) => assert_eq!(python_result, x),
            None => panic!("No value returned for part 2"),
        }
    }
}
