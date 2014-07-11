# revision 15878
# category Package
# catalog-ctan /fonts/ps-type1/esint
# catalog-date 2008-01-16 21:31:11 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-esint-type1
Version:	20080116
Release:	8
Summary:	Font esint10 in Type 1 format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/ps-type1/esint
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esint-type1.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esint-type1.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080116-2
+ Revision: 751576
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080116-1
+ Revision: 718365
- texlive-esint-type1
- texlive-esint-type1
- texlive-esint-type1
- texlive-esint-type1

