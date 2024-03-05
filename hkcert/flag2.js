import fs from 'fs';
import express from 'express';
import session from 'express-session';
import multer from 'multer';
import QRCode from 'qrcode-svg';
import jsQR from 'jsqr';
import sharp from 'sharp';

const flag0 = 'hkcert23{ST_ST&s4_STegan0graphy--STeg0}';

async function encodeQR(data){
    return new QRCode(flag0).svg();
  }

async function decodeQR(svg) {
  try {
    const { data, info } = await sharp(Buffer.from(svg)).ensureAlpha().raw().toBuffer({ resolveWithObject: true });
    const output = await jsQR(new Uint8ClampedArray(data.buffer), info.width, info.height);
    return output.data;
  } catch (e) {
    return null;
  }
}

// Read the SVG file
const svgFilePath = 'flag1st.svg';
const svgFileContent = fs.readFileSync(svgFilePath, 'utf-8');

// Call decodeQR with the SVG file content
decodeQR(svgFileContent)
  .then((decodedData) => {
    console.log(decodedData);
    // Do something with the decoded data
  })
  .catch((error) => {
    console.error(error);
  });

encodeQR(flag0)
  .then((decodedData) => {
    console.log(decodedData);
    // Do something with the decoded data
  })
  .catch((error) => {
    console.error(error);
  });