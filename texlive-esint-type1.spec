Name:		texlive-esint-type1
Version:	15878
Release:	2
Summary:	Font esint10 in Type 1 format
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/ps-type1/esint
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esint-type1.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esint-type1.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-esint

%description
This is Eddie Saudrais's font esint10 in Adobe Type 1 format.
The Adobe Type 1 implementation was generated from the original
MetaFont using mftrace. This distribution does not contain the
TFM files that are necessary to use the fonts with TeX; the TFM
files can be generated from the Metafont sources obtained by
following the instructions in the normal way.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/esint-type1/config.esint
%{_texmfdistdir}/fonts/map/dvips/esint-type1/esint.map
%{_texmfdistdir}/fonts/type1/public/esint-type1/esint10.pfb
%{_texmfdistdir}/tex/plain/esint-type1/esint.tex
%doc %{_texmfdistdir}/doc/fonts/esint-type1/README
%doc %{_texmfdistdir}/doc/fonts/esint-type1/README.plainTeX
%doc %{_texmfdistdir}/doc/fonts/esint-type1/table.pdf
%doc %{_texmfdistdir}/doc/fonts/esint-type1/table.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts tex doc %{buildroot}%{_texmfdistdir}
