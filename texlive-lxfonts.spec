Name:		texlive-lxfonts
Version:	32354
Release:	1
Summary:	Set of slide fonts based on CM
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/lxfonts
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lxfonts.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lxfonts.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lxfonts.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle contains the traditional slides fonts revised to be
completely usable both as text fonts and mathematics fonts;
they are fully integrate with the new operators, letters,
symbols and extensible delimiter fonts, as well as with the AMS
fonts, all redone with the same stylistic parameters.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/lxfonts/lxfonts.map
%{_texmfdistdir}/fonts/source/public/lxfonts/lamsya.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lamsyb.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lasymbols.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lbigacc.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lbigdel.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lbigop.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lbsymbols.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lcmbsy8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lcmex8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lcmmi8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lcmmib8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lcmsy8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/leclb8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lecli8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/leclo8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/leclq8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lexroman.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lexslides.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/llasy.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/llasy8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/llasyb8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/llcmss8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/llcmssb8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/llcmssi8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/llcmsso8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lmathex.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lmathit.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lmathsy.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lmsam8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lmsbm8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lroman.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/ltclb8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/ltcli8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/ltclo8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/ltclq8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/ltxsymb.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lxbbase.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lxbbold.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lxbcaps.mf
%{_texmfdistdir}/fonts/tfm/public/lxfonts/lcmbsy8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/lcmex8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/lcmmi8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/lcmmib8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/lcmsy8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/leclb8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/lecli8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/leclo8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/leclq8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/llasy8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/llasyb8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/llcmss8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/llcmssb8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/llcmssi8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/llcmsso8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/lmsam8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/lmsbm8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/ltclb8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/ltcli8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/ltclo8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/ltclq8.tfm
%{_texmfdistdir}/fonts/type1/public/lxfonts/lcmbsy8.pfb
%{_texmfdistdir}/fonts/type1/public/lxfonts/lcmex8.pfb
%{_texmfdistdir}/fonts/type1/public/lxfonts/lcmmi8.pfb
%{_texmfdistdir}/fonts/type1/public/lxfonts/lcmmib8.pfb
%{_texmfdistdir}/fonts/type1/public/lxfonts/lcmsy8.pfb
%{_texmfdistdir}/fonts/type1/public/lxfonts/leclb8.pfb
%{_texmfdistdir}/fonts/type1/public/lxfonts/lecli8.pfb
%{_texmfdistdir}/fonts/type1/public/lxfonts/leclo8.pfb
%{_texmfdistdir}/fonts/type1/public/lxfonts/leclq8.pfb
%{_texmfdistdir}/fonts/type1/public/lxfonts/llasy8.pfb
%{_texmfdistdir}/fonts/type1/public/lxfonts/llasyb8.pfb
%{_texmfdistdir}/fonts/type1/public/lxfonts/llcmss8.pfb
%{_texmfdistdir}/fonts/type1/public/lxfonts/llcmssb8.pfb
%{_texmfdistdir}/fonts/type1/public/lxfonts/llcmssi8.pfb
%{_texmfdistdir}/fonts/type1/public/lxfonts/llcmsso8.pfb
%{_texmfdistdir}/fonts/type1/public/lxfonts/lmsam8.pfb
%{_texmfdistdir}/fonts/type1/public/lxfonts/lmsbm8.pfb
%{_texmfdistdir}/fonts/type1/public/lxfonts/ltclb8.pfb
%{_texmfdistdir}/fonts/type1/public/lxfonts/ltcli8.pfb
%{_texmfdistdir}/fonts/type1/public/lxfonts/ltclo8.pfb
%{_texmfdistdir}/fonts/type1/public/lxfonts/ltclq8.pfb
%{_texmfdistdir}/tex/latex/lxfonts/lgrllcmss.fd
%{_texmfdistdir}/tex/latex/lxfonts/lgrllcmtt.fd
%{_texmfdistdir}/tex/latex/lxfonts/lxfonts.sty
%{_texmfdistdir}/tex/latex/lxfonts/omlllcmm.fd
%{_texmfdistdir}/tex/latex/lxfonts/omsllcmsy.fd
%{_texmfdistdir}/tex/latex/lxfonts/omxllcmex.fd
%{_texmfdistdir}/tex/latex/lxfonts/ot1llcmss.fd
%{_texmfdistdir}/tex/latex/lxfonts/ot1llcmtt.fd
%{_texmfdistdir}/tex/latex/lxfonts/t1llcmss.fd
%{_texmfdistdir}/tex/latex/lxfonts/t1llcmtt.fd
%{_texmfdistdir}/tex/latex/lxfonts/ts1llcmss.fd
%{_texmfdistdir}/tex/latex/lxfonts/ulllasy.fd
%{_texmfdistdir}/tex/latex/lxfonts/ulmsa.fd
%{_texmfdistdir}/tex/latex/lxfonts/ulmsb.fd
%doc %{_texmfdistdir}/doc/fonts/lxfonts/LXfonts-demo.pdf
%doc %{_texmfdistdir}/doc/fonts/lxfonts/LXfonts-demo.tex
%doc %{_texmfdistdir}/doc/fonts/lxfonts/LXfonts.readme
%doc %{_texmfdistdir}/doc/fonts/lxfonts/README
%doc %{_texmfdistdir}/doc/fonts/lxfonts/lxfonts.pdf
%doc %{_texmfdistdir}/doc/fonts/lxfonts/manifest.txt
#- source
%doc %{_texmfdistdir}/source/fonts/lxfonts/lxfonts.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
