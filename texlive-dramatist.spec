Name:		texlive-dramatist
Version:	1.2d
Release:	1
Summary:	Typeset dramas, both in verse and in prose
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dramatist
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dramatist.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dramatist.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dramatist.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package is intended for typesetting drama of any length.
It provides two environments for typesetting dialogues in prose
or in verse; new document divisions corresponding to acts and
scenes; macros that control the appearance of characters and
stage directions; and automatic generation of a `dramatis
personae' list.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dramatist/dramatist.sty
%doc %{_texmfdistdir}/doc/latex/dramatist/README
%doc %{_texmfdistdir}/doc/latex/dramatist/dramatist.pdf
%doc %{_texmfdistdir}/doc/latex/dramatist/marlowe-poemscol.tex
%doc %{_texmfdistdir}/doc/latex/dramatist/marlowe-verse.tex
%doc %{_texmfdistdir}/doc/latex/dramatist/schiller.tex
#- source
%doc %{_texmfdistdir}/source/latex/dramatist/dramatist.dtx
%doc %{_texmfdistdir}/source/latex/dramatist/dramatist.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
