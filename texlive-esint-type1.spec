%global tl_name esint-type1
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Font esint10 in Type 1 format
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/ps-type1/esint
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/esint-type1.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/esint-type1.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(esint)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is Eddie Saudrais's font esint10 in Adobe Type 1 format. The Adobe
Type 1 implementation was generated from the original Metafont using
mftrace. This distribution does not contain the TFM files that are
necessary to use the fonts with TeX; the TFM files can be generated from
the Metafont sources obtained by following the instructions in the
normal way.

