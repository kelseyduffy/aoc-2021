use std::fmt::Error;

pub enum Fault {
    Corrupt(u64),
    Incomplete(u64),
}

pub fn get_puzzle_input() -> Result<Vec<Vec<char>>,Error> {
    Ok(std::fs::read_to_string(String::from("input.txt")).expect("Failed to open file")
        .lines()
        .map(|line| line.chars().collect())
        .collect())
}

pub fn get_scores() -> (u64, u64) {
    score_input(get_puzzle_input().unwrap())
}

pub fn score_input(lines: Vec<Vec<char>>) -> (u64, u64) {
    let mut corrupted_scores = 0;
    let mut incomplete_scores = Vec::new();

    for line in lines {
        match score_line(line) {
            Some(Fault::Corrupt(x)) => corrupted_scores += x,
            Some(Fault::Incomplete(x)) => incomplete_scores.push(x),
            _ => (),
        };
    }

    incomplete_scores.sort();

    (corrupted_scores, incomplete_scores[incomplete_scores.len() / 2])
}

pub fn score_line(line: Vec<char>) -> Option<Fault> {
    
    use std::collections::HashMap;

    if line.len() == 0 {
        return None
    }

    let expected_closing_chars = HashMap::from([
        ('(', ')'),
        ('[', ']'),
        ('{', '}'),
        ('<', '>'),
    ]);

    let char_scores = HashMap::from([
        // Incomplete lines
        ('(', 1),
        ('[', 2),
        ('{', 3),
        ('<', 4),
        // Corrupted lines
        (')', 3),
        (']', 57),
        ('}', 1197),
        ('>', 25137),
    ]);

    let mut current_stack = Vec::new();

    for this_char in line {
        if expected_closing_chars.contains_key(&this_char) {
            current_stack.push(this_char);
        }
        else {
            if let Some(popped_char) = current_stack.pop() {
                if let Some(expected_char) = expected_closing_chars.get(&popped_char) {
                    if this_char != *expected_char {
                        if let Some(score) = char_scores.get(&this_char) {
                            return Some(Fault::Corrupt(*score))
                        };
                    }
                };
            };  
        }
    }

    // If it makes it this far, it's not corrupted. Unwind the stack and count the scores

    let mut score = 0;

    let mut stack_empty = false;

    while !stack_empty {
        if let Some(popped_char) = current_stack.pop() {
            if let Some(this_score) = char_scores.get(&popped_char) {
                score *= 5;
                score += this_score;
            };
        } else {
            stack_empty = true;
        };
    }

    Some(Fault::Incomplete(score))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let (rust_p1, rustp2) = get_scores();
        let (python_p1, pythonp2) = (411471, 3122628974);
        
        assert_eq!(rust_p1, python_p1, "part 1 failed");
        assert_eq!(rustp2, pythonp2, "part 2 failed");
    }
}
