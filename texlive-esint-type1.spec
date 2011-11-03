# revision 15878
# category Package
# catalog-ctan /fonts/ps-type1/esint
# catalog-date 2008-01-16 21:31:11 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-esint-type1
Version:	20080116
Release:	1
Summary:	Font esint10 in Type 1 format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/ps-type1/esint
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esint-type1.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esint-type1.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-esint
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This is Eddie Saudrais's font esint10 in Adobe Type 1 format.
The Adobe Type 1 implementation was generated from the original
MetaFont using mftrace. This distribution does not contain the
TFM files that are necessary to use the fonts with TeX; the TFM
files can be generated from the Metafont sources obtained by
following the instructions in the normal way.

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
%{_texmfdistdir}/dvips/esint-type1/config.esint
%{_texmfdistdir}/fonts/map/dvips/esint-type1/esint.map
%{_texmfdistdir}/fonts/type1/public/esint-type1/esint10.pfb
%{_texmfdistdir}/tex/plain/esint-type1/esint.tex
%doc %{_texmfdistdir}/doc/fonts/esint-type1/README
%doc %{_texmfdistdir}/doc/fonts/esint-type1/README.plainTeX
%doc %{_texmfdistdir}/doc/fonts/esint-type1/table.pdf
%doc %{_texmfdistdir}/doc/fonts/esint-type1/table.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
