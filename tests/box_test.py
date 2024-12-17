import sys

from bible import BibleRef
from file_utils import iterate_jsons
from translation import Translation


def test_box_interval_property(translation):
    for box, box_ref in translation.iterate_on_boxes():
        length = box.length()
        prev_ref = None
        for index, (bible_ref, _) in enumerate(box.iterate()):
            if index != 0 and index != length - 1:
                assert not bible_ref.is_cut_ref(), f'Cut verse in the middle of a box. box_ref={box_ref}'
            if index == 0:
                if bible_ref.is_cut_ref():
                    assert (bible_ref.x == 2) or (
                                length == 1), f'Unexpected cut ref at the start of a box. box_ref={box_ref} ref={bible_ref}'
                prev_ref = bible_ref
                continue
            if index == length - 1:
                if bible_ref.is_cut_ref():
                    assert bible_ref.x == 1, f'Unexpected cut ref at the end of a box. box_ref={box_ref} ref={bible_ref}'
                bible_ref = bible_ref.get_base_ref()
            assert prev_ref.next() == bible_ref, f'Box interval property failed. box_ref={box_ref} prev_ref={prev_ref} ref={bible_ref}'
            prev_ref = bible_ref


def test_main_body_partition_property(translation):
    all_main_body_refs = set()
    for box, box_ref in translation.iterate_on_main_boxes():
        for bible_ref, _ in box.iterate():
            assert bible_ref not in all_main_body_refs, f'Ref multiple times in main body. ref={bible_ref}'
            all_main_body_refs.add(bible_ref)
    for ref in all_main_body_refs:
        if ref.is_cut_ref():
            base_ref = ref.get_base_ref()
            assert base_ref not in all_main_body_refs, f'Both cut ref and base ref are in main body. cut_ref={ref} base_ref={base_ref}'
            ref_pair = ref.get_cut_ref_pair()
            assert ref_pair in all_main_body_refs, f'Cut ref pair is missing. ref={ref} ref_pair={ref_pair}'

    all_base_refs = set()
    curr = BibleRef.begin()
    while curr != BibleRef.end():
        all_base_refs.add(curr)
        curr = curr.next()

    for r in all_base_refs:
        if r not in all_main_body_refs:
            a, b = r.cut_base_ref()
            assert a in all_main_body_refs and b in all_main_body_refs, f'Missing base reference. ref={r}'

    for r in all_main_body_refs:
        if r.is_cut_ref():
            assert r.get_base_ref() in all_base_refs, f'Unknown main body ref. ref={r}'
        else:
            assert r in all_base_refs, f'Unknown main body ref. ref={r}'


def test_main_body_ordering(translation):
    for e in range(4):
        start = True
        prev = None
        for box, box_ref in translation.iterate_on_main_boxes():
            if e == box_ref.e:
                if start:
                    prev = box.get_sec()
                    start = False
                    continue
                curr = box.get_sec()
                assert prev.begin < curr.begin and (
                        prev.end == curr.begin or prev.end == curr.begin.get_base_ref()), f'Main body boxes are not fitting. box_ref={box_ref} prev={prev} curr={curr}'
                prev = curr


def main():
    translation_folder = sys.argv[1]
    bible_json, _ = next(iterate_jsons(translation_folder))
    translation = Translation(bible_json)
    test_box_interval_property(translation)
    test_main_body_partition_property(translation)
    test_main_body_ordering(translation)
    curr_cuts = translation.get_cut_verses()
    print(curr_cuts)
    secondary_cuts = [BibleRef(2, 6, 14, 0), BibleRef(0, 26, 60, 0), BibleRef(0, 13, 57, 0), BibleRef(2, 3, 2, 0), BibleRef(0, 12, 15, 0), BibleRef(1, 1, 45, 0), BibleRef(1, 6, 6, 0), BibleRef(0, 13, 2, 0), BibleRef(1, 4, 1, 0), BibleRef(1, 6, 6, 0), BibleRef(2, 8, 18, 0), BibleRef(2, 6, 20, 0), BibleRef(3, 15, 20, 0), BibleRef(0, 12, 15, 0), BibleRef(0, 13, 2, 0), BibleRef(1, 4, 1, 0), BibleRef(1, 6, 56, 0), BibleRef(3, 16, 2, 0), BibleRef(2, 9, 48, 0), BibleRef(0, 21, 31, 0), BibleRef(1, 6, 6, 0), BibleRef(2, 9, 50, 0), BibleRef(3, 9, 39, 0), BibleRef(1, 8, 17, 0), BibleRef(1, 6, 56, 0), BibleRef(0, 16, 13, 0), BibleRef(1, 8, 27, 0), BibleRef(2, 9, 18, 0), BibleRef(0, 14, 12, 0), BibleRef(1, 5, 29, 0), BibleRef(0, 13, 54, 0), BibleRef(0, 13, 57, 0), BibleRef(1, 6, 2, 0), BibleRef(2, 9, 10, 0), BibleRef(0, 10, 2, 0), BibleRef(2, 6, 13, 0), BibleRef(2, 6, 14, 0), BibleRef(2, 24, 6, 0), BibleRef(2, 9, 43, 0), BibleRef(2, 3, 22, 0), BibleRef(0, 17, 9, 0), BibleRef(1, 9, 9, 0), BibleRef(2, 24, 6, 0), BibleRef(2, 18, 14, 0), BibleRef(1, 6, 6, 0), BibleRef(2, 9, 48, 0), BibleRef(0, 14, 12, 0), BibleRef(2, 9, 10, 0), BibleRef(2, 9, 50, 0), BibleRef(0, 16, 2, 0), BibleRef(1, 12, 38, 0), BibleRef(0, 25, 20, 0), BibleRef(0, 9, 30, 0), BibleRef(2, 18, 43, 0), BibleRef(2, 4, 22, 0), BibleRef(1, 8, 17, 0), BibleRef(2, 8, 10, 0), BibleRef(1, 9, 35, 0), BibleRef(2, 9, 43, 0), BibleRef(2, 24, 6, 0), BibleRef(2, 8, 18, 0), BibleRef(2, 21, 5, 0), BibleRef(0, 21, 19, 0), BibleRef(1, 12, 12, 0), BibleRef(1, 12, 34, 0), BibleRef(1, 12, 34, 0), BibleRef(2, 9, 48, 0), BibleRef(2, 18, 14, 0), BibleRef(2, 21, 8, 0), BibleRef(2, 8, 18, 0), BibleRef(1, 8, 38, 0), BibleRef(2, 9, 26, 0), BibleRef(2, 3, 22, 0), BibleRef(1, 8, 17, 0), BibleRef(2, 8, 21, 0), BibleRef(3, 8, 38, 0), BibleRef(0, 27, 26, 0), BibleRef(1, 15, 15, 0), BibleRef(2, 23, 33, 0), BibleRef(1, 15, 36, 0)]
    new_cuts = set()
    for ref in secondary_cuts:
        if ref not in curr_cuts:
            new_cuts.add(ref)
    print(sorted(new_cuts))
    print(len(new_cuts))

if __name__ == '__main__':
    main()
