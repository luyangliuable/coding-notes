extern crate sha2;
use sha2::{Sha256, Digest};
use rand::Rng;

fn hash_password(password: &str, salt: &[u8]) -> Vec<u8> {
    let mut hasher = Sha256::new();
    hasher.input(salt);
    hasher.input(password.as_bytes());
    hasher.result().to_vec()
}

fn main() {
    let password = "mysecretpassword";
    let mut rng = rand::thread_rng();
    let mut salt = [0u8; 32];
    rng.fill(&mut salt[..]);
    let hashed_password = hash_password(password, &salt);
    println!("Hashed password: {:x?}", hashed_password);
    println!("Salt: {:x?}", salt);
}
