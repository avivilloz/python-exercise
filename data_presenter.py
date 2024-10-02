from tabulate import tabulate
from typing import List, Tuple, Dict

class DataPresenter:
    def present_global_stats(self, stats: List[Tuple[str, int, float]]):
        """Present global statistics in a tabular format."""
        table_data = [
            [i+1, country_code, count, f"{percentage:.1f}%"]
            for i, (country_code, count, percentage) in enumerate(stats)
        ]
        headers = ["#", "Country Code", "Number Of Universities", "Percent Of Total"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

    def present_country_stats(self, stats: List[Tuple[str, int, float]]):
        """Present country statistics in a tabular format."""
        table_data = [
            [i+1, province, count, f"{percentage:.1f}%"]
            for i, (province, count, percentage) in enumerate(stats)
        ]
        headers = ["#", "Province", "Number Of Universities", "Percent Of Total"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

    def present_province_universities(self, universities: List[Dict]):
        """Present universities in a province in a tabular format."""
        table_data = [
            [i+1, uni['name'], uni['web_pages'][0] if uni['web_pages'] else 'N/A']
            for i, uni in enumerate(universities)
        ]
        headers = ["#", "Name", "URL"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

    def present_search_results(self, universities: List[Dict]):
        """Present search results in a tabular format."""
        table_data = [
            [
                i+1, 
                uni['name'], 
                uni['alpha_two_code'], 
                uni.get('state-province', 'N/A'), 
                uni['web_pages'][0] if uni['web_pages'] else 'N/A'
            ] for i, uni in enumerate(universities)
        ]
        headers = ["#", "Name", "Country Code", "Province", "URL"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))