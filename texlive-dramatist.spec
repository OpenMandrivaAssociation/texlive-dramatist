Name:		texlive-dramatist
Version:	35866
Release:	1
Summary:	Typeset dramas, both in verse and in prose
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dramatist
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dramatist.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dramatist.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dramatist.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/dramatist
%doc %{_texmfdistdir}/doc/latex/dramatist
#- source
%doc %{_texmfdistdir}/source/latex/dramatist

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
