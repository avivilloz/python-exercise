import requests
from collections import defaultdict
from typing import List, Tuple, Dict


class UniversityData:
    API_URL = "http://universities.hipolabs.com/search"

    def __init__(self):
        self.data = self.fetch_data()

    def fetch_data(self) -> List[Dict]:
        """Fetch university data from the API."""
        response = requests.get(self.API_URL)
        response.raise_for_status()
        return response.json()

    def get_global_stats(self) -> List[Tuple[str, int, float]]:
        """Get global statistics of universities by country."""
        country_counts = defaultdict(int)
        for uni in self.data:
            country_counts[uni["alpha_two_code"]] += 1

        total_unis = len(self.data)
        stats = [
            (country_code, count, (count / total_unis) * 100)
            for country_code, count in country_counts.items()
        ]

        return sorted(stats, key=lambda x: x[-1], reverse=True)

    def get_country_stats(self, country_code: str) -> List[Tuple[str, int, float]]:
        """Get statistics of universities by province for a specific country."""
        country_unis = [
            uni
            for uni in self.data
            if uni["alpha_two_code"] == country_code.upper()
            or uni["country"].lower() == country_code.lower()
        ]

        province_counts = defaultdict(int)
        for uni in country_unis:
            province_counts[uni.get("state-province", "Unknown")] += 1

        total_country_unis = len(country_unis)
        stats = [
            (province, count, (count / total_country_unis) * 100)
            for province, count in province_counts.items()
        ]

        return sorted(stats, key=lambda x: x[-1], reverse=True)

    def get_province_universities(self, country_code: str, province: str) -> List[Dict]:
        """Get universities in a specific province of a country."""
        return sorted(
            [
                uni
                for uni in self.data
                if (
                    uni["alpha_two_code"] == country_code.upper()
                    or uni["country"].lower() == country_code.lower()
                )
                and (uni.get("state-province") or "").lower() == province.lower()
            ],
            key=lambda x: x["name"],
        )

    def search_universities(self, query: str) -> List[Dict]:
        """Search for universities by name."""
        return sorted(
            [uni for uni in self.data if query.lower() in uni["name"].lower()],
            key=lambda x: x["name"],
        )
