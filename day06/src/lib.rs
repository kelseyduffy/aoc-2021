use std::fmt::Error;

pub fn part1() -> Option<i64> {
    count_the_fishes(get_puzzle_input().unwrap(), 80)
}

pub fn part2() -> Option<i64> {
    count_the_fishes(get_puzzle_input().unwrap(), 256)
}

fn count_the_fishes(fishes: Vec<i32>, days: i32) -> Option<i64> {
    
    if fishes.len() == 0 {
        return None
    }

    let mut fish_counts = [0; 9];

    for fish in fishes {
        fish_counts[fish as usize] += 1;
    };

    for _ in 0..days {
        let mut new_fishes = [0; 9];

        for i in 1..9 {
            new_fishes[i - 1] = fish_counts[i];
        }

        new_fishes[8] = fish_counts[0];
        new_fishes[6] += fish_counts[0];

        fish_counts = new_fishes;
    };

    Some(fish_counts.iter().sum())

}

fn get_puzzle_input() -> Result<Vec<i32>, Error> {
    Ok(std::fs::read_to_string(String::from("input.txt")).expect("Failed to open file")
        .split(',')
        .map(|x| x.parse().unwrap())
        .collect())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn part1_works() {
        let rust_result = part1();
        let python_result: i64 = 352195;

        match rust_result {
            Some(x) => assert_eq!(x, python_result),
            None => panic!("Part 1 did not return an answer")
        }
        
    }

    #[test]
    fn part2_works() {
        let rust_result = part2();
        let python_result: i64 = 1600306001288;
        
        match rust_result {
            Some(x) => assert_eq!(x, python_result),
            None => panic!("Part 2 did not return an answer")
        }
    }
}
