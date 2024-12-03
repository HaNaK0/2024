use std::{
    fs::File,
    io::{BufRead, BufReader},
};

use anyhow::anyhow;

const DATA_PATH: &str = "data.txt";

#[derive(PartialEq, Eq)]
enum ChangeDirection {
    Rising,
    Falling,
    Neither,
}

impl ChangeDirection {
    fn calculate<T>(first: &T, second: &T) -> anyhow::Result<Self>
    where
        T: PartialEq + PartialOrd,
    {
        if first == second {
            Ok(ChangeDirection::Neither)
        } else if first < second {
            Ok(ChangeDirection::Rising)
        } else if first > second {
            Ok(ChangeDirection::Falling)
        } else {
            Err(anyhow!("Should not get here"))
        }
    }
}

fn main() -> anyhow::Result<()> {
    let result = read_data()?
        .filter(|l| {
            let split: Vec<i32> = l.split(" ").map(|c| c.parse::<i32>().unwrap()).collect();

            if !check_line(split.clone()) {
                (0..split.len())
                    .map(|i| {
                        check_line(split.iter().enumerate().filter_map(|(index, n)| {
                            if i == index {
                                None
                            } else {
                                Some(*n)
                            }
                        }))
                    })
                    .find(|b| *b)
                    .is_some()
            } else {
                true
            }
        })
        .count();

    println!("{result}");
    Ok(())
}

fn check_line<I>(line: I) -> bool
where
    I: IntoIterator<Item = i32>,
{
    let mut line = line.into_iter();

    let first: i32 = line.nth(0).unwrap();
    let mut previous = line.nth(0).unwrap();
    let expected_change = ChangeDirection::calculate(&first, &previous).unwrap();

    if expected_change == ChangeDirection::Neither || (first - previous).abs() > 3 {
        return false;
    }

    for num in line {
        let current_change = ChangeDirection::calculate(&previous, &num).unwrap();

        if current_change != expected_change || (num - previous).abs() > 3 {
            return false;
        }

        previous = num
    }

    return true;
}

fn read_data() -> anyhow::Result<impl Iterator<Item = String>> {
    let file = File::open(DATA_PATH)?;

    let bufreader = BufReader::new(file);
    let iter = bufreader.lines().map(|l| l.unwrap());

    Ok(iter)
}
