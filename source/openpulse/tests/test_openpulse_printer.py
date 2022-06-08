import textwrap

import pytest
from openpulse.parser import parse
from openpulse.printer import dumps


@pytest.mark.parametrize(
    "p",
    [
        "b = capture(ro_kernel, q0_capture_frame);",
        "barrier q;",
        "delay[10.0ns] q;",
        "play(wf1, frame1);",
        """
        cal {
          set_frequency(1000000000, frame1);
        }
        """,
        """
        cal {
          set_phase(1.1, phase);
        }
        """,
        """
        cal {
          waveform sx_wf = drag(0.2 + 0.1 * Im, 160.0dt, 40.0dt, 0.05);
        }
        """,
        """
        defcal rz(angle[20] theta) $q {
          return shift_phase(drive($q), -theta);
        }
        """,
        """
        defcal x90() $q {
        }
        """,
        """
        defcal x90() $q {
          set_phase(0.22 * 2 * pi, frame1);
        }
        """,
        """
        if (i == 0) {
          do_if_zero();
        }
        """,
        """
        if (some_function() > 1) {
          do_if_gt_one();
        } else {
          do_otherwise();
        }
        """,
        """
        for x in [1:2:10] {
          step();
        }
        """,
        """
        while (i < 10) {
          i -= 1;
        }
        """,
        """
        def my_subroutine(int[32] i, qubit q) {
          f(i, q);
        }
        """,
        """
        def my_subroutine(int[32] i, qubit q) -> bit {
          return measure q;
        }
        """,
        "extern my_extern(float[32], duration) -> duration;",
        "H $0;",
        "v = (x + y) * z;",  # test add parens when needed
        "v = z / (x * y);",
        "v = x * y / z;",
        "v = x ** (y / z);",
        "v = x ** y / z;",
        "v = (x / z) ** y;",
        """
        cal {
          set_frequency(1000000000, frame1);
        }
        """,
        """
        defcal rz(angle[20] theta) $q {
          return shift_phase(drive($q), -theta);
        }
        """,
        """
        defcal x90() $q {
        }
        """,
    ],
)
def test_print(p: str):
    program = parse(p)
    p2 = dumps(program)
    assert p2.strip() == textwrap.dedent(p).strip()