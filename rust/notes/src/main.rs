mod args;
use args::Args;
use image::{ io::Reader, DynamicImage, ImageFormat, imageops::FilterType::Triangle, GenericImageView, ImageError };
use std::fmt::Error;
use std::sync::mpsc::RecvError;
use std::{io::BufReader, fs::File};
use std::convert::TryInto;

#[derive(Debug)] // Derive debug trait for the args struct
enum ImageDataErrors {
    DifferentImageFormats,
    BufferTooSmall,
    UnableToReadImageFromPath(std::io::Error),
    UnableToFormatImage(String),
    UnableToDecodeImage(ImageError),
    UnableToSaveImage(ImageError)
}


struct FloatingImage {
    width: u32,
    height: u32,
    data: Vec<u8>,
    name: String,
}


impl FloatingImage {
    fn new(width: u32, height: u32, name: String) -> FloatingImage {
        // let buffer_capacity = 3_655_744;
        let buffer_capacity = width * height * 4; // Multiply by 4 because of rgba value

        let buffer = Vec::with_capacity(buffer_capacity.try_into().unwrap());

        FloatingImage {
            width: width,
            height: height,
            data: buffer,
            name: name
        }
    }

    fn set_data(&mut self, data: Vec<u8>) -> Result<(), ImageDataErrors> {

        if data.len() > self.data.capacity() {
            return Err(ImageDataErrors::BufferTooSmall);
        }

        self.data = data;
        Ok(())
    }
}


fn main() -> Result<(), ImageDataErrors> {
    let args = Args::new();
    let (image_1, image_format_1) = find_image_from_path(args.image_1)?;
    let (image_2, image_format_2) = find_image_from_path(args.image_2)?;

    if image_format_1 != image_format_2 {
        return Err(ImageDataErrors::DifferentImageFormats);
    }

    // println!("{:?}, {:?}", image_format_1, image_format_2);
    let (image_1, image_2) = standardize_size(image_1, image_2);
    let mut output = FloatingImage::new(image_1.width(), image_1.height(), args.output);

    let combined_data = combine_images(image_1, image_2);
    // println!("{:?}, {}, {:?}, {}", output.height, output.width, output.data, output.name);

    output.set_data(combined_data)?;

    if let Err(e) = image::save_buffer_with_format(&output.name, &output.data, output.width, output.height, image::ColorType::Rgba8, image_format_1) {
        return Err(ImageDataErrors::UnableToSaveImage(e));
    }

    Ok(())
}


fn combine_images(image_1: DynamicImage, image_2: DynamicImage) -> Vec<u8> {
    let vec_1 = image_1.to_rgba8()
.into_vec();
    let vec_2 = image_2.to_rgba8().into_vec();

    alternate_pixels(vec_1, vec_2)
}

fn alternate_pixels(vec_1: Vec<u8>, vec_2: Vec<u8>) -> Vec<u8> {
    let mut combined_data = vec![0u8; vec_1.len()];

    let mut i = 0;
    while i < vec_1.len() {
        if i % 8 == 0 {
            combined_data.splice(i..= i + 3, set_rgba(&vec_1, i, i + 3));
        } else {
            combined_data.splice(i..= i + 3, set_rgba(&vec_2, i, i + 3));
        }

        i += 4;
    }

    combined_data
}


fn set_rgba(vec: &Vec<u8>, start: usize, end: usize) -> Vec<u8> {
    let mut rgba = Vec::new();

    for i in start..=end {
        let val = match vec.get(i) {
            Some(d) => *d, // If there is some value d
            None => panic!("Index is out of bounds.")
        };

        rgba.push(val);
    };

    rgba
}


fn get_smallest_dimension(dim_1: (u32, u32), dim_2: (u32, u32)) -> (u32, u32) {
    let pix_1 = dim_1.0 * dim_1.1;
    let pix_2 = dim_2.0 * dim_2.1;

    return if pix_1 < pix_2 { dim_1 } else { dim_2 };
}


fn standardize_size(image_1: DynamicImage, image_2: DynamicImage) -> (DynamicImage, DynamicImage) {
    let (width, height) = get_smallest_dimension(image_1.dimensions(), image_2.dimensions());
    println!("width: {width}, height: {height}.\n");

    if image_2.dimensions() == (width, height) {
        (image_1.resize_exact(width, height, Triangle), image_2)
    } else {
        (image_1, image_2.resize_exact(width, height, Triangle))
    }

}


fn find_image_from_path(path: String) -> Result<(DynamicImage, ImageFormat), ImageDataErrors> {
    match Reader::open(&path) {
        Ok(image_reader) => {
            if let Some(image_format) = image_reader.format() {
                match image_reader.decode() {
                    Ok(image) => Ok((image, image_format)),
                    Err(e) =>  Err(ImageDataErrors::UnableToDecodeImage(e))
                }
            } else {
                return Err(ImageDataErrors::UnableToFormatImage(path));
            }
        },
        Err(e) => Err(ImageDataErrors::UnableToReadImageFromPath(e))
    }
}


// To compile and release program
// cargo build --release

