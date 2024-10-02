#!/usr/bin/env python3

import argparse
import sys
from university_data import UniversityData
from data_presenter import DataPresenter

def main():
    parser = argparse.ArgumentParser(description="University data summarization tool")
    parser.add_argument("--global", action="store_true", help="Show global university statistics")
    parser.add_argument("--country", type=str, help="Show statistics for a specific country")
    parser.add_argument("--province", type=str, help="Show statistics for a specific province")
    parser.add_argument("--search", type=str, help="Search for universities by name")

    args = parser.parse_args()

    data = UniversityData()
    presenter = DataPresenter()

    if getattr(args, 'global'):
        global_stats = data.get_global_stats()
        presenter.present_global_stats(global_stats)
    elif args.country and args.province:
        province_unis = data.get_province_universities(args.country, args.province)
        presenter.present_province_universities(province_unis)
    elif args.country:
        country_stats = data.get_country_stats(args.country)
        presenter.present_country_stats(country_stats)
    elif args.search:
        search_results = data.search_universities(args.search)
        presenter.present_search_results(search_results)
    else:
        print("Please provide a valid argument. Use --help for more information.")
        sys.exit(1)

if __name__ == "__main__":
    main()