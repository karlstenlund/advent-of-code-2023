# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/5

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 5

    @answer(111627841)
    def part_1(self) -> int:
        seeds = self.input[0].split(":")[1].split()
        seeds = [int(s) for s in seeds]
        almanacs = self.create_almanacs()
        locations = []
        for seed in seeds:
            for almanac in almanacs:
                seed = almanac.translate(seed)
            locations.append(seed)
        return min(locations)

    # @answer(1234)
    def part_2(self) -> int:
        seeds = self.input[0].split(":")[1].split()
        seeds = [int(s) for s in seeds]
        seeds = self.split_list_chunks(seeds, 2)
        seeds = [(s[0], s[1]) for s in seeds]

        almanacs = self.create_almanacs()
        for alm in almanacs:
            new_seeds = []
            for seed in seeds:
                new_seeds.extend(alm.translate_range(seed))
            seeds = new_seeds
        return min([s[0] for s in seeds])

    def split_list_chunks(self, lst: list, chunk_size: int) -> list[list]:
        return [lst[i : i + chunk_size] for i in range(0, len(lst), chunk_size)]

    def create_almanacs(self):
        part = []
        almanacs = []
        for line in self.input[2:]:
            if line == "":
                almanacs.append(Almanac(part[0], part[1:]))
                part = []
            else:
                part.append(line)
        almanacs.append(Almanac(part[0], part[1:]))
        return almanacs


class Almanac:
    """
    A mapping of source to destination addresses.
    """

    def __init__(self, header: str, data: list[str]):
        self.header = header
        self.translations = self.create_translation(data)

    def __repr__(self):
        return f"Almanac({self.header}, {self.translations})"

    def create_translation(self, data: list[str]) -> [tuple[int, int]]:
        translations = []
        for line in data:
            d_start, s_start, length = line.split()
            translations.append((int(s_start), int(d_start), int(length)))
        return translations

    def translate(self, source: int) -> int:
        """
        Translate a source address to a destination address.
        """
        for s_start, d_start, length in self.translations:
            if s_start + length >= source >= s_start:
                return source + d_start - s_start
        return source

    def translate_range(self, source: (int, int)) -> [(int, int)]:
        """
        Translate a range of source addresses to a range of destination addresses.
        """
        sources = [source]
        translated = []
        sorted_translations = sorted(self.translations, key=lambda x: x[0])
        for trans_start, d_start, length in sorted_translations:
            if not bool(sources):
                
                return translated
            for s, l in sources:
                new_sources = []
                source_end = s + l
                trans_end = trans_start + length
                # If whole range is inside translation
                if (
                    trans_end >= s >= trans_start
                    and trans_end >= source_end >= trans_start
                ):
                    
                    translated.append((s + d_start - trans_start, l))
                # If start of range is inside translation but end is not
                elif trans_end >= s >= trans_start and source_end >= trans_end:
                    translated.append((s + d_start - trans_start, trans_end - s))
                    # Add remaining ranges
                    if source_end > trans_end:
                        new_sources.append((trans_end, source_end - trans_end))
                    break
                # If end of range is inside translation but start is not
                elif trans_end >= source_end >= trans_start and s <= trans_start:
                    
                    translated.append((d_start, source_end - trans_start))
                    # Remove translated range from new_sources
                    # Add remaining ranges
                    if s < trans_start:
                        new_sources.append((s, trans_start - s))
                # If translation is inside range
                elif trans_start > s and source_end > trans_end:
                    
                    translated.append((d_start, length))
                    # Add remaining ranges
                    if trans_start > s:
                        new_sources.append((s, trans_start - s))
                    if source_end > trans_end:
                        new_sources.append(
                            (trans_end, source_end - trans_start - length)
                        )
                    break
                else:
                    
                    new_sources.append((s, l))
            sources = new_sources
        return translated + sources

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
