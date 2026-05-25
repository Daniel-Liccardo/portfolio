#!/usr/bin/env python3
"""macOS native OCR — uses Vision framework, zero API cost, offline, zh+en+ja."""
import sys
import Quartz
import Vision
from Foundation import NSURL

def ocr_image(image_path: str) -> str:
    """Extract text from image using macOS Vision framework."""
    url = NSURL.fileURLWithPath_(image_path)
    ci_image = Quartz.CIImage.imageWithContentsOfURL_(url)
    if ci_image is None:
        return f"[ERROR: Cannot load image {image_path}]"

    request = Vision.VNRecognizeTextRequest.alloc().init()
    request.setRecognitionLevel_(Vision.VNRequestTextRecognitionLevelAccurate)
    request.setRecognitionLanguages_(["zh-Hans", "zh-Hant", "en", "ja"])
    request.setUsesLanguageCorrection_(True)

    handler = Vision.VNImageRequestHandler.alloc().initWithCIImage_options_(ci_image, None)
    success = handler.performRequests_error_([request], None)
    if not success:
        return "[ERROR: Vision OCR failed]"

    results = request.results()
    if not results:
        return "[No text found]"

    lines = []
    for obs in results:
        top = obs.topCandidates_(1)
        if top and len(top) > 0:
            text = top[0].string()
            if text:
                lines.append(text)
    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 .mac-ocr.py <image-path>")
        sys.exit(1)
    print(ocr_image(sys.argv[1]))
