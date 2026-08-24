from pathlib import Path

base = Path(r"C:\Users\fang\AppData\Local\Temp\zed_bib_test")
base.mkdir(parents=True, exist_ok=True)

main_tex = r"""\documentclass{article}
\begin{document}
This is a citation test \cite{knuth1984}.
\bibliographystyle{plain}
\bibliography{refs}
\end{document}
"""

refs_bib = r"""@book{knuth1984,
  author  = {Donald E. Knuth},
  title   = {The {TeX}book},
  publisher = {Addison-Wesley},
  year    = {1984}
}
"""

(base / "main.tex").write_text(main_tex, encoding="utf-8")
(base / "refs.bib").write_text(refs_bib, encoding="utf-8")
print("files written in", base)
print("main.tex bytes:", (base / "main.tex").stat().st_size)
print("refs.bib bytes:", (base / "refs.bib").stat().st_size)
