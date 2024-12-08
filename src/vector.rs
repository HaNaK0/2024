use std::ops::{Add, Mul, Sub};

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

    fn get_x_iterator() -> impl Iterator<Item = Vector> {
        [(-1, -1), (1, 1), (-1, 1), (1, -1)]
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
