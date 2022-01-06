use std::collections::HashSet;
use std::fmt::Error;

pub struct Line {
    input: Vec<HashSet<u8>>,
    output: Vec<HashSet<u8>>,
}

impl Line {
    pub fn new(line: &str) -> Line {
        let (input_string, output_string) = line.trim().split_once(" | ").unwrap();

        let input_parts = input_string.trim().split(' ');
        let output_parts = output_string.trim().split(' ');

        let input: Vec<HashSet<u8>> = input_parts
            .map(|num| string_to_hashset_bytes(num))
            .collect();

        let output: Vec<HashSet<u8>> = output_parts
            .map(|num| string_to_hashset_bytes(num))
            .collect();

        Line { input, output }
    }

    fn count_1478s(&self) -> i32 {
        self.output
            .iter()
            .filter(|x| [2, 3, 4, 7].contains(&x.len()))
            .count()
            .try_into()
            .unwrap()
    }

    fn decode_output(&self) -> Result<i32, ()> {
        
        if self.input.len() != 10 {
            return Err(());
        }

        let mut fivers: Vec<HashSet<u8>> = Vec::new();
        let mut sixers: Vec<HashSet<u8>> = Vec::new();

        let mut cf = HashSet::new();
        let mut bcdf = HashSet::new();
        let mut acf = HashSet::new();
        let mut abcdefg = HashSet::new();
        
        for in_digit in self.input {

            if in_digit.len() == 2 {
                cf.extend(&in_digit);
            }

            else if in_digit.len() == 3 {
                acf.extend(&in_digit);
            }

            else if in_digit.len() == 4 {
                bcdf.extend(&in_digit);
            }

            else if in_digit.len() == 5 {
                fivers.append(&in_digit.iter().copied().collect());
            }

            else if in_digit.len() == 6 {
                sixers.append(&in_digit.iter().copied().collect());
            }

            else if in_digit.len() == 7 {
                abcdefg.extend(&in_digit);
            }
        }

        let adg: HashSet<_> = fivers[0].intersection(&fivers[1]).copied().collect().intersection(&fivers[2]).copied().collect();
        let abfg: HashSet<_> = sixers[0].intersection(&sixers[1]).copied().collect().intersection(&sixers[2]).copied().collect();
        let ag: HashSet<_> = adg.intersection(&abfg).copied().collect();

        let a: HashSet<_> = acf.difference(&cf).collect();
        let bd: HashSet<_> = bcdf.difference(&cf).collect();
        let eg: HashSet<_> = abcdefg.difference(&bcdf).collect().difference(&a).collect();
        let g: HashSet<_> = ag.difference(&a).collect();
        let e: HashSet<_> = eg.difference(&g).collect();
        let d: HashSet<_> = adg.difference(&ag).collect();
        let b: HashSet<_> = bd.difference(&d).collect();

        let mut out_string = String::from("");

        for out_digit in self.output {
            
            if out_digit.len() == 2 {
                out_string = out_string + "1";
            }

            else if out_digit.len() == 3 {
                out_string = out_string + "7";
            }

            else if out_digit.len() == 4 {
                out_string = out_string + "4";
            }

            else if out_digit.len() == 7 {
                out_string = out_string + "8";
            }

            else if out_digit.len() == 5 {
                
                if e.is_subset(&out_digit) {
                    out_string = out_string + "2";
                }
                
                else if b.is_subset(&out_digit) {
                    out_string = out_string + "5";
                }

                else {
                    out_string = out_string + "3";
                }
            }

            else {
                if !d.is_subset(&out_digit) {
                    out_string = out_string + "0";
                }

                else if e.is_subset(&out_digit) {
                    out_string = out_string + "6";
                }

                else {
                    out_string = out_string + "9";
                }
            }
        }

        Ok(out_string.parse().expect("Failed to output number"))
    }
}

pub fn part1() -> Option<i32> {
    Some(
        get_puzzle_input()
            .unwrap()
            .iter()
            .map(|line| line.count_1478s())
            .sum(),
    )
}

pub fn part2() -> Option<i32> {
    let lines = get_puzzle_input().unwrap();

    if lines.is_empty() {
        return None;
    }

    Some(lines.iter().map(|line| line.decode_output().unwrap()).sum())
}

fn get_puzzle_input() -> Result<Vec<Line>, Error> {
    eprintln!("Getting puzzle input");

    Ok(std::fs::read_to_string(String::from("input.txt"))
        .expect("Failed to open file")
        .lines()
        .map(|line| Line::new(line))
        .collect())
}

fn string_to_hashset_bytes(input: &str) -> HashSet<u8> {
    let mut letters = HashSet::new();

    for byte in input.bytes() {
        letters.insert(byte);
    }

    letters
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn part1_works() {
        let rust_result = part1().expect("No answer was returned!");
        let python_result = 521;

        assert_eq!(rust_result, python_result);
    }

    #[test]
    fn part2_works() {
        let rust_result = part2().expect("No answer was returned!");
        let python_result = 1016804;

        assert_eq!(rust_result, python_result);
    }
}
