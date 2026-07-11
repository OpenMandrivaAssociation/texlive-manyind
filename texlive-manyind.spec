%global tl_name manyind
%global tl_revision 49874

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Provides support for many indexes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/manyind
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/manyind.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/manyind.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides support for many indexes, leaving all the
bookkeeping to LaTeX and makeindex. No extra programs or files are
needed. One runs latex and makeindex as if there is just one index. In
the main file one puts commands like \setindex{main} to steer the flow.
Some features of makeindex may no longer work.

