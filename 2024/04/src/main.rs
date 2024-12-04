use std::fs;

fn main() {
    println!("Part 1: {}", solve_p1());
}

fn check_for_needle(padded_lines: &Vec<String>, needle: &Vec<char>) -> i32 {
    // Directions in (x, y) format right - x+, down - y+, down-right - x+y+, up-right - x+y-
    let directions = vec![(1, 0), (0, 1), (1, 1), (1, -1)];

    let mut sum = 0;
    for y in 1..padded_lines.len() {
        for x in 1..padded_lines[y].len() {
            if padded_lines[y].chars().nth(x).unwrap() == needle[0] {
                for (dx, dy) in &directions {
                    for c in needle {
                        let cur_x = (dx + (x as i32)) as usize;
                        let cur_y = (dy + (y as i32)) as usize;
                        if padded_lines[cur_y].chars().nth(cur_x).unwrap() != *c {
                            break;
                        } else {
                            sum += 1;
                            break;
                        }
                    }
                }
            }
        }
    }

    sum
}

fn solve_p1() -> i32 {
    let contents = fs::read_to_string("src/input_p1.txt");
    // Create padding before and after every line
    let lines = contents.unwrap().lines().map(|x| format!(".{x}.")).collect::<Vec<String>>();
    // Create padding before and after the whole input
    let mut padded_lines = vec![".".repeat(lines[0].len())];
    padded_lines.extend(lines);
    padded_lines.push(padded_lines[0].clone());
    let padded_lines_reverse = padded_lines.iter().map(|x| x.chars().rev().collect::<String>()).collect::<Vec<String>>();
    println!("{:?}", padded_lines);
    println!("---");
    println!("{:?}", padded_lines_reverse);

    let needle = vec!['X', 'M', 'A', 'S'];
    let mut sum = 0;
    sum += check_for_needle(&padded_lines, &needle);
    sum += check_for_needle(&padded_lines_reverse, &needle);




    sum
}