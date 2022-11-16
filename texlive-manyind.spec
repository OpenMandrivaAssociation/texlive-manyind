Name:		texlive-manyind
Version:	49874
Release:	1
Summary:	Provides support for many indexes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/manyind
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/manyind.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/manyind.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides support for many indexes, leaving all the
bookkeeping to LaTeX and makeindex. No extra programs or files
are needed. One runs latex and makeindex as if there is just
one index. In the main file one puts commands like
\setindex{main} to steer the flow. Some features of makeindex
may no longer work.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/manyind
%doc %{_texmfdistdir}/doc/latex/manyind

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
