use std::fmt::Error;

pub struct Point {
    x: u32,
    y: u32,
}

pub enum Fold {
    X(u32),
    Y(u32),
}

impl Point {
    pub fn new(input: &str) -> Point {
        let parts: Vec<&str> = input.trim().split(',').collect();
        Point { 
            x: parts[0].parse().unwrap(),
            y: parts[1].parse().unwrap(),
        }
    }
}

impl Fold {
    pub fn new(input: &str) -> Fold {
        let instruction: String = input.trim().chars().skip(11).collect();
        let parts: Vec<&str> = instruction.split('=').collect();

        let amount:u32 = parts[1].parse().unwrap();

        match parts[0] {
            "x" => Fold::X(amount),
            "y" => Fold::Y(amount),
            _ => unreachable!(),
        }
    }
}

pub fn part1() -> Option<u32> {
    let (points, folds) = get_puzzle_input().unwrap();

    Some(0)
}

pub fn part2() -> Option<String> {
    let (points, folds) = get_puzzle_input().unwrap();

    Some(String::new())
}

fn get_puzzle_input() -> Result<(Vec<Point>, Vec<Fold>), Error> {
    
    let (point_list, fold_list) = std::fs::read_to_string(String::from("input.txt"))
        .expect("Failed to open file")
        .split_once("\n\n")
        .unwrap();
    
    let points: Vec<Point> = point_list
        .lines()
        .map(Point::new)
        .collect();

    let folds: Vec<Fold> = fold_list
        .lines()
        .map(Fold::new)
        .collect();
    
    Ok((points, folds))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn part1_works() {
        let rust_result = part1().expect("No answer was returned!");
        let python_result = 716;

        assert_eq!(rust_result, python_result);
    }

    #[test]
    fn part2_works() {
        let rust_result = part2().expect("No answer was returned!");
        let python_result = "
###  ###   ##  #  # #### ###  #    ###
#  # #  # #  # # #  #    #  # #    #  #
#  # #  # #    ##   ###  ###  #    #  #
###  ###  #    # #  #    #  # #    ###
# #  #    #  # # #  #    #  # #    # #
#  # #     ##  #  # #    ###  #### #  #
";

        assert_eq!(rust_result, python_result);
    }
}
