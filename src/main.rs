use std::{
    fs::File,
    io::{BufRead, BufReader},
};

const DATA_PATH: &str = "data.txt";

fn main() -> anyhow::Result<()> {
    let mut list_1 = vec![];
    let mut list_2 = vec![];

    for line in read_data()? {
        let mut split = line.split("   ").map(|s| s.parse::<i32>().unwrap());

        list_1.push(split.next().unwrap());
        list_2.push(split.next().unwrap());
    }

    list_1.sort();
    list_2.sort();

    let result: i32 = list_1
        .iter()
        .zip(list_2.iter())
        .map(|(num_1, num_2)| (num_2 - num_1).abs())
        .sum();

    println!("{result}");

    Ok(())
}

fn read_data() -> anyhow::Result<impl Iterator<Item = String>> {
    let file = File::open(DATA_PATH)?;

    let bufreader = BufReader::new(file);
    let iter = bufreader.lines().map(|l| l.unwrap());

    Ok(iter)
}
