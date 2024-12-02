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
            let mut split = l.split(" ").map(|c| c.parse::<i32>().unwrap());

            let first: i32 = split.nth(0).unwrap();
            let mut previous = split.nth(0).unwrap();
            let expected_change = ChangeDirection::calculate(&first, &previous).unwrap();

            if expected_change == ChangeDirection::Neither {
                return false;
            }

            for num in split {
                let current_change = ChangeDirection::calculate(&previous, &num).unwrap();

                if current_change != expected_change || (num - previous).abs() > 3 {
                    return false;
                }

                previous = num
            }

            println!("{l}");

            true
        })
        .count();

    println!("{result}");
    Ok(())
}

fn read_data() -> anyhow::Result<impl Iterator<Item = String>> {
    let file = File::open(DATA_PATH)?;

    let bufreader = BufReader::new(file);
    let iter = bufreader.lines().map(|l| l.unwrap());

    Ok(iter)
}
