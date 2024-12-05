use std::{
    char,
    fs::File,
    io::{BufRead, BufReader},
    ops::{Add, Mul, Sub},
};

const DATA_PATH: &str = "data.txt";

#[derive(Clone, Copy)]
struct Vector {
    x: i64,
    y: i64,
}

impl Vector {
    fn new_from_index(index: usize, columns: usize) -> Self {
        Self {
            x: (index % columns) as i64,
            y: (index / columns) as i64,
        }
    }

    fn get_index(&self, columns: usize, rows: usize) -> Option<usize> {
        if self.x >= 0 && self.y >= 0 && self.x < columns as i64 && self.y < rows as i64 {
            Some((self.x as usize) + (self.y as usize) * columns)
        } else {
            None
        }
    }

    fn get_direction_iterator() -> impl Iterator<Item = Vector> {
        [
            (-1, -1),
            (0, -1),
            (1, -1),
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
        ]
        .iter()
        .map(|v| Self::from(*v))
    }
}

impl<T> From<(T, T)> for Vector
where
    T: Into<i64>,
{
    fn from(value: (T, T)) -> Self {
        Self {
            x: value.0.into(),
            y: value.1.into(),
        }
    }
}

impl Add for Vector {
    type Output = Self;

    fn add(self, rhs: Self) -> Self::Output {
        Self {
            x: self.x + rhs.x,
            y: self.y + rhs.y,
        }
    }
}

impl Sub for Vector {
    type Output = Self;

    fn sub(self, rhs: Self) -> Self::Output {
        Self {
            x: self.x - rhs.x,
            y: self.y - rhs.y,
        }
    }
}

impl<T> Mul<T> for Vector
where
    T: Mul<i64, Output = i64> + Copy,
{
    type Output = Vector;

    fn mul(self, rhs: T) -> Self::Output {
        Self {
            x: rhs * self.x,
            y: rhs * self.y,
        }
    }
}

fn main() -> anyhow::Result<()> {
    let chars = read_data()?
        .map(|line| line.chars().collect::<Vec<char>>())
        .collect::<Vec<Vec<char>>>();

    let flat_chars: Vec<&char> = chars.iter().flatten().collect();

    let columns = chars[0].len();
    let rows = chars.len();

    let result: usize = chars
        .iter()
        .flatten()
        .enumerate()
        .filter_map(|(i, &c)| if c == 'X' { Some(i) } else { None })
        .map(|i| {
            let current_position = Vector::new_from_index(i, columns);
            Vector::get_direction_iterator()
                .filter_map(|v| get_word(4, &v, &current_position, columns, rows, &flat_chars))
                .filter(|s| s == "XMAS")
                .inspect(|s| println!("{s}"))
                .count()
        })
        .sum();

    println!("{result}");
    Ok(())
}

fn get_word(
    len: usize,
    vector: &Vector,
    origin: &Vector,
    columns: usize,
    rows: usize,
    chars: &Vec<&char>,
) -> Option<String> {
    let string: String = (0..len)
        .map_while(|i| {
            let pos = *origin + *vector * (i as i64);
            if let Some(index) = pos.get_index(columns, rows) {
                Some(chars[index])
            } else {
                None
            }
        })
        .collect();

    if string.len() == len {
        Some(string)
    } else {
        None
    }
}

fn read_data() -> anyhow::Result<impl Iterator<Item = String>> {
    let file = File::open(DATA_PATH)?;

    let bufreader = BufReader::new(file);
    let iter = bufreader.lines().map(|l| l.unwrap());

    Ok(iter)
}
