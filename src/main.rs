use std::{
    char,
    fs::File,
    io::{BufRead, BufReader},
};

const DATA_PATH: &str = "data.txt";

#[allow(dead_code)]
mod vector;

fn main() -> anyhow::Result<()> {
    todo!()
}

fn read_data() -> anyhow::Result<impl Iterator<Item = String>> {
    let file = File::open(DATA_PATH)?;

    let bufreader = BufReader::new(file);
    let iter = bufreader.lines().map(|l| l.unwrap());

    Ok(iter)
}
