#!/usr/bin/env python3

# imports
import argparse
import os

from pathlib import Path

import yt_dlp


def main(url: str, output_dir: os.PathLike, padding: int):
    
    # make the output dir if it does not exist
    output_dir = Path(os.path.expanduser(output_dir))
    if not output_dir.exists():
        output_dir.mkdir(parents=True)

    # define the output template and yt-dlp options
    output_template = (
        f"{output_dir}/"
        f"%(playlist_title)s - "
        f"%(playlist_index)0{padding}d - "
        f"%(title)s.%(ext)s"
    )

    ydl_opts = {
        "outtmpl": output_template,
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mkv",
        "ignoreerrors": True,
        "windowsfilenames": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl: # type: ignore
        ydl.download([url])


if __name__ == "__main__":
    # define the argument parser and add inputs
    parser = argparse.ArgumentParser(
        description="Download a YouTube playlist with organized filenames."
    )

    parser.add_argument(
        "url",
        type=str,
        help="YouTube playlist URL"
    )

    parser.add_argument(
        "-o", "--output-dir",
        type=str,
        default=".",
        help="Output directory (default: current directory)"
    )

    parser.add_argument(
        "-p", "--padding",
        type=int,
        default=2,
        help="Number of digits for playlist numbering (default: 2)"
    )
    
    args = parser.parse_args()

    if args.padding < 1:
        parser.error("Padding must be at least 1.")
        
    # pass the args to main
    main(
        url=args.url,
        output_dir=args.output_dir,
        padding=args.padding
    )
