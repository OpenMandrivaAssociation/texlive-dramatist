# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/dramatist
# catalog-date 2006-12-01 14:16:52 +0100
# catalog-license gpl
# catalog-version 1.2d
Name:		texlive-dramatist
Version:	1.2d
Release:	10
Summary:	Typeset dramas, both in verse and in prose
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dramatist
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dramatist.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dramatist.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dramatist.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is intended for typesetting drama of any length.
It provides two environments for typesetting dialogues in prose
or in verse; new document divisions corresponding to acts and
scenes; macros that control the appearance of characters and
stage directions; and automatic generation of a `dramatis
personae' list.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2d-2
+ Revision: 751088
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2d-1
+ Revision: 718260
- texlive-dramatist
- texlive-dramatist
- texlive-dramatist
- texlive-dramatist

