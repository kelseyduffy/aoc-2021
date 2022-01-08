use std::collections::HashSet;
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
        let mut line_iter = input.trim().split(' ').skip(2);
        let parts: Vec<&str> = line_iter.next().unwrap().split('=').collect();

        let amount: u32 = parts[1].parse().unwrap();

        match parts[0] {
            "x" => Fold::X(amount),
            "y" => Fold::Y(amount),
            _ => unreachable!(),
        }
    }
}

pub fn fold_point(point: &Point, folds: &Vec<Fold>) -> (u32, u32) {
    let (mut x, mut y) = (point.x, point.y);

    folds.iter().for_each(|fold| match fold {
        Fold::X(val) if val < &x => x = 2 * val - x,
        Fold::Y(val) if val < &y => y = 2 * val - y,
        _ => (),
    });

    (x, y)
}

pub fn single_fold_point(point: &Point, fold: &Fold) -> (u32, u32) {
    let (mut x, mut y) = (point.x, point.y);

    match fold {
        Fold::X(val) if val < &x => x = 2 * val - x,
        Fold::Y(val) if val < &y => y = 2 * val - y,
        _ => (),
    };

    (x, y)
}

pub fn part1() -> Option<u32> {
    let (points, folds) = get_puzzle_input().unwrap();

    let set: HashSet<(u32, u32)> = points
        .iter()
        //.map(|point| fold_point(&point, &folds[..1].copied().to_vec()))
        .map(|point| single_fold_point(&point, &folds[0]))
        .collect();

    Some(set.len() as u32)
}

pub fn part2() -> Option<String> {
    let (points, folds) = get_puzzle_input().unwrap();

    let set: HashSet<(u32, u32)> = points
        .iter()
        .map(|point| fold_point(&point, &folds))
        .collect();

    let mut answer = String::new();
    answer += "\n";

    let max_x = set.iter().map(|&(x, _)| x).max().unwrap();
    let max_y = set.iter().map(|&(_, y)| y).max().unwrap();

    for y in 0..max_y + 1 {
        for x in 0..max_x + 1 {
            match set.contains(&(x, y)) {
                true => answer += "#",
                false => answer += " ",
            };
        }
        answer += "\n";
    }

    Some(answer)
}

fn get_puzzle_input() -> Result<(Vec<Point>, Vec<Fold>), Error> {
    let file_contents =
        std::fs::read_to_string(String::from("input.txt")).expect("Failed to open file");

    let mut file_iter = file_contents.split("\n\n");

    let points: Vec<Point> = file_iter.next().unwrap().lines().map(Point::new).collect();

    let folds: Vec<Fold> = file_iter.next().unwrap().lines().map(Fold::new).collect();

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
