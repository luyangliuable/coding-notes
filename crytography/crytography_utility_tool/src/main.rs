extern crate openssl;
use openssl::sha::Sha256;
use rand::Rng;
use checksum::sha256_with_salt;

fn hash_password(password: &str, salt: &[u8]) -> Vec<u8> {
    let mut hasher = Sha256::new();
    hasher.update(salt);
    hasher.update(password.as_bytes());
    hasher.finish().to_vec()
}


fn line_to_words(line: &str) -> Vec<String> {
    line.split_whitespace().map(str::to_string).collect()
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
