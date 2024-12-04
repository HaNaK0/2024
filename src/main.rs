use std::{
    char,
    fs::File,
    io::{BufRead, BufReader},
    iter::Peekable,
};

const DATA_PATH: &str = "data.txt";

fn main() -> anyhow::Result<()> {
    let lines = read_data()?;

    let result: i32 = lines
        .map(|line| {
            let mut chars = line.chars().peekable();

            let mut sum = 0;

            while chars.peek().is_some() {
                if let Some((num_1, num_2)) = read_mul(&mut chars) {
                    sum += num_1 * num_2;
                } else {
                    chars.next();
                }
            }

            sum
        })
        .sum();

    print!("{result}");

    Ok(())
}

fn read_mul<T>(chars: &mut Peekable<T>) -> Option<(i32, i32)>
where
    T: Iterator<Item = char>,
{
    if !parse_string(chars, "mul(") {
        return None;
    }

    let first_num = read_num(chars);

    if first_num.is_none() {
        return None;
    }

    if chars.next_if_eq(&',').is_none() {
        return None;
    }

    let second_num = read_num(chars);

    if second_num.is_none() {
        return None;
    }

    if chars.next_if_eq(&')').is_none() {
        return None;
    }

    Some((first_num.unwrap(), second_num.unwrap()))
}

fn read_num<T>(chars: &mut Peekable<T>) -> Option<i32>
where
    T: Iterator<Item = char>,
{
    let mut out = String::new();
    while let Some(c) = chars.next_if(|c| c.is_numeric()) {
        out.push(c.clone());
    }

    if out.is_empty() {
        None
    } else {
        Some(out.parse().unwrap())
    }
}

fn parse_string<I, S>(chars: &mut Peekable<I>, string: &S) -> bool
where
    I: Iterator<Item = char>,
    S: AsRef<str> + ?Sized,
{
    for c in string.as_ref().chars() {
        if chars.next_if_eq(&c).is_none() {
            return false;
        }
    }

    true
}

fn read_data() -> anyhow::Result<impl Iterator<Item = String>> {
    let file = File::open(DATA_PATH)?;

    let bufreader = BufReader::new(file);
    let iter = bufreader.lines().map(|l| l.unwrap());

    Ok(iter)
}
