import sys

from file_utils import iterate_jsons
from translation import Box, Translation


def test_box_interval_property(translation):
    for box, box_ref in translation.iterate_on_boxes():
        b = Box(box, box_ref.e)
        length = b.length()
        prev_ref = None
        for index, (bible_ref, _) in enumerate(b.iterate()):
            if index != 0 and index != length - 1:
                assert not bible_ref.is_cut_ref(), f'Cut verse in the middle of a box. box_ref={box_ref}'
            if index == 0:
                prev_ref = bible_ref
                continue
            if index == length - 1:
                if bible_ref.is_cut_ref():
                    assert bible_ref.x == 1, f'Unexpected cut ref at the end of a box. box_ref={box_ref} ref={bible_ref}'
                bible_ref = bible_ref.get_base_ref()
            assert prev_ref.next() == bible_ref, f'Box interval property failed. box_ref={box_ref} prev_ref={prev_ref} ref={bible_ref}'
            prev_ref = bible_ref

def main():
    translation_folder = sys.argv[1]
    bible_json, _ = next(iterate_jsons(translation_folder))
    translation = Translation(bible_json)
    test_box_interval_property(translation)

if __name__ == '__main__':
    main()
