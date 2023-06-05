import re


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if re.search(r'^<iframe src="((https|http)?://)?(www\.)?youtube\.com/embed/.+"></iframe>$', s, flags = re.IGNORECASE):
        return (re.sub( r'^<iframe src="((https|http)?://)?(www\.)?', 'https://', str(s).replace('youtube.com/embed/', 'youtu.be/'))).replace('"></iframe>', '')
    else:
        return None


if __name__ == "__main__":
    main()