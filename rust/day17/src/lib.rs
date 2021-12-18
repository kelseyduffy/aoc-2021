use std::fmt::Error;

pub fn part1() -> Option<i32> {
    
    // xmin xmax ymin ymax
    let target = get_puzzle_input().unwrap();
    
    if target.len() == 0 {
        return None
    }
    
    Some((0..-target[2]).fold(0, |a, b| a + b))
}

pub fn part2() -> Option<i32> {
    let target = get_puzzle_input().unwrap();
    
    if target.len() == 0 {
        return None
    }

    let mut lowest_x = 0;
    let mut total = 0;

    while total < target[0] {
        lowest_x += 1;
        total += lowest_x;
    }

    let mut hits = 0;

    for x in lowest_x..(target[1] + 1) {
        for y in target[2]..(-target[1] + 1) {
            match check_hit(x, y, target) {
                Some(true) => hits += 1,
                _ => (),
            }
        }
    }
    Some(hits)
}

fn check_hit(mut x_vel: i32, mut y_vel: i32, target: Vec<i32>) -> Option<bool> {
    
    let mut x = 0;
    let mut y = 0;

    if target.len() != 4 {
        return None
    }
    
    while x <= target[1] && y >= target[2] {
        if target[0] <= x && x <= target[1] && target[2] <= y && y <= target[3] {
            return Some(true)
        }

        x += x_vel;
        y += y_vel;

        y_vel -= 1;
        if x_vel > 0 {
            x_vel -= 1
        } 
    }

    Some(false)
}

pub fn get_puzzle_input() -> Result<Vec<i32>,Error> {
    Ok(std::fs::read_to_string(String::from("input.txt")).expect("Failed to open file")
        .replace("target area: x=","")
        .replace("..",",")
        .replace(" y=","")
        .split(',')
        .map(|x| x.parse().unwrap())
        .collect())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn part1_works() {
        let python_result = 2701;
        let rust_result = part1();

        match rust_result {
            Some(x) => assert_eq!(python_result, x),
            None => panic!("No value returned for part 1"),
        }
    }

    #[test]
    fn part2_works() {
        let python_result = 1070;
        let rust_result = part2();

        match rust_result {
            Some(x) => assert_eq!(python_result, x),
            None => panic!("No value returned for part 2"),
        }
    }
}
