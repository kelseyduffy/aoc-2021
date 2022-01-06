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
            .map(string_to_hashset_bytes)
            .collect();

        let output: Vec<HashSet<u8>> = output_parts
            .map(string_to_hashset_bytes)
            .collect();

        Line { input, output }
    }

    fn count_1478s(&self) -> i32 {
        self.output
            .iter()
            .filter(|x| matches!(x.len(), 2 | 3 | 4 | 7))
            .count() as i32
    }

    fn decode_output(&self) -> Result<i32, ()> {
        if self.input.len() != 10 {
            return Err(());
        }

        //let mut fivers: Vec<HashSet<u8>> = Vec::new();
        //let mut sixers: Vec<HashSet<u8>> = Vec::new();

        let mut five_1 = HashSet::new();
        let mut five_2 = HashSet::new();
        let mut five_3 = HashSet::new();
        let mut six_1 = HashSet::new();
        let mut six_2 = HashSet::new();
        let mut six_3 = HashSet::new();

        let mut cf = HashSet::new();
        let mut bcdf = HashSet::new();
        let mut acf = HashSet::new();
        let mut abcdefg = HashSet::new();

        for in_digit in &self.input {
            if in_digit.len() == 2 {
                cf.extend(in_digit);
            } else if in_digit.len() == 3 {
                acf.extend(in_digit);
            } else if in_digit.len() == 4 {
                bcdf.extend(in_digit);
            } else if in_digit.len() == 5 {
                if five_1.is_empty() {
                    five_1.extend(in_digit);
                } else if five_2.is_empty() {
                    five_2.extend(in_digit);
                } else {
                    five_3.extend(in_digit);
                }
                //fivers.append(&in_digit.iter().copied().collect());
            } else if in_digit.len() == 6 {
                if six_1.is_empty() {
                    six_1.extend(in_digit);
                } else if six_2.is_empty() {
                    six_2.extend(in_digit);
                } else {
                    six_3.extend(in_digit);
                }
                //sixers.append(&in_digit.iter().copied().collect());
            } else if in_digit.len() == 7 {
                abcdefg.extend(in_digit);
            }
        }

        //let adg: HashSet<u8> = fivers[0].intersection(&fivers[1]).copied().collect().intersection(&fivers[2]).copied().collect();
        let mut adg: HashSet<u8> = five_1.intersection(&five_2).copied().collect();
        adg = adg.intersection(&five_3).copied().collect();
        //let abfg: HashSet<u8> = sixers[0].intersection(&sixers[1]).copied().collect().intersection(&sixers[2]).copied().collect();
        let mut abfg: HashSet<u8> = six_1.intersection(&six_2).copied().collect();
        abfg = abfg.intersection(&six_3).copied().collect();

        let ag: HashSet<u8> = adg.intersection(&abfg).copied().collect();

        let a: HashSet<u8> = acf.difference(&cf).copied().collect();
        let bd: HashSet<u8> = bcdf.difference(&cf).copied().collect();
        let mut eg: HashSet<u8> = abcdefg.difference(&bcdf).copied().collect();
        eg = eg.difference(&a).copied().collect();
        let g: HashSet<u8> = ag.difference(&a).copied().collect();
        let e: HashSet<u8> = eg.difference(&g).copied().collect();
        let d: HashSet<u8> = adg.difference(&ag).copied().collect();
        let b: HashSet<u8> = bd.difference(&d).copied().collect();

        let mut out_string = String::new();

        for out_digit in &self.output {
            if out_digit.len() == 2 {
                out_string += "1";
            } else if out_digit.len() == 3 {
                out_string += "7";
            } else if out_digit.len() == 4 {
                out_string += "4";
            } else if out_digit.len() == 7 {
                out_string += "8";
            } else if out_digit.len() == 5 {
                if e.is_subset(out_digit) {
                    out_string += "2";
                } else if b.is_subset(out_digit) {
                    out_string += "5";
                } else {
                    out_string += "3";
                }
            } else if !d.is_subset(out_digit) {
                out_string += "0";
            } else if e.is_subset(out_digit) {
                out_string += "6";
            } else {
                out_string += "9";
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
        .map(Line::new)
        .collect())
}

fn string_to_hashset_bytes(input: &str) -> HashSet<u8> {
    input.bytes().collect()
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
