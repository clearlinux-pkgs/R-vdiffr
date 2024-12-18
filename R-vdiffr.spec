#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: 5424026
#
Name     : R-vdiffr
Version  : 1.0.8
Release  : 18
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/vdiffr_1.0.8.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/vdiffr_1.0.8.tar.gz
Summary  : Visual Regression Testing and Graphical Diffing
Group    : Development/Tools
License  : MIT
Requires: R-vdiffr-lib = %{version}-%{release}
Requires: R-vdiffr-license = %{version}-%{release}
Requires: R-cpp11
Requires: R-diffobj
Requires: R-glue
Requires: R-htmltools
Requires: R-lifecycle
Requires: R-rlang
Requires: R-testthat
Requires: R-xml2
BuildRequires : R-cpp11
BuildRequires : R-diffobj
BuildRequires : R-glue
BuildRequires : R-htmltools
BuildRequires : R-lifecycle
BuildRequires : R-rlang
BuildRequires : R-testthat
BuildRequires : R-xml2
BuildRequires : buildreq-R
BuildRequires : libpng-dev

%description
add graphical unit tests. It provides a Shiny application to manage
    the test cases.

%package lib
Summary: lib components for the R-vdiffr package.
Group: Libraries
Requires: R-vdiffr-license = %{version}-%{release}

%description lib
lib components for the R-vdiffr package.


%package license
Summary: license components for the R-vdiffr package.
Group: Default

%description license
license components for the R-vdiffr package.


%prep
%setup -q -n vdiffr
pushd ..
cp -a vdiffr buildavx2
popd
pushd ..
cp -a vdiffr buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1731652447

%install
export SOURCE_DATE_EPOCH=1731652447
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-vdiffr
cp %{_builddir}/vdiffr/LICENSE.note %{buildroot}/usr/share/package-licenses/R-vdiffr/0318f6c080dce561fe3e8896ba4b6f2cee4b0f3d || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/vdiffr/DESCRIPTION
/usr/lib64/R/library/vdiffr/INDEX
/usr/lib64/R/library/vdiffr/LICENSE
/usr/lib64/R/library/vdiffr/Meta/Rd.rds
/usr/lib64/R/library/vdiffr/Meta/features.rds
/usr/lib64/R/library/vdiffr/Meta/hsearch.rds
/usr/lib64/R/library/vdiffr/Meta/links.rds
/usr/lib64/R/library/vdiffr/Meta/nsInfo.rds
/usr/lib64/R/library/vdiffr/Meta/package.rds
/usr/lib64/R/library/vdiffr/NAMESPACE
/usr/lib64/R/library/vdiffr/NEWS.md
/usr/lib64/R/library/vdiffr/R/vdiffr
/usr/lib64/R/library/vdiffr/R/vdiffr.rdb
/usr/lib64/R/library/vdiffr/R/vdiffr.rdx
/usr/lib64/R/library/vdiffr/create_glyph_dims.R
/usr/lib64/R/library/vdiffr/help/AnIndex
/usr/lib64/R/library/vdiffr/help/aliases.rds
/usr/lib64/R/library/vdiffr/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/vdiffr/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/vdiffr/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/vdiffr/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/vdiffr/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/vdiffr/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/vdiffr/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/vdiffr/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/vdiffr/help/paths.rds
/usr/lib64/R/library/vdiffr/help/vdiffr.rdb
/usr/lib64/R/library/vdiffr/help/vdiffr.rdx
/usr/lib64/R/library/vdiffr/html/00Index.html
/usr/lib64/R/library/vdiffr/html/R.css
/usr/lib64/R/library/vdiffr/tests/testthat.R
/usr/lib64/R/library/vdiffr/tests/testthat/_snaps/bar/expect-doppelganger/variant.svg
/usr/lib64/R/library/vdiffr/tests/testthat/_snaps/expect-doppelganger/base-doppelganger-with-symbol.svg
/usr/lib64/R/library/vdiffr/tests/testthat/_snaps/expect-doppelganger/grid-doppelganger.svg
/usr/lib64/R/library/vdiffr/tests/testthat/_snaps/expect-doppelganger/grob.svg
/usr/lib64/R/library/vdiffr/tests/testthat/_snaps/expect-doppelganger/myplot.svg
/usr/lib64/R/library/vdiffr/tests/testthat/_snaps/expect-doppelganger/myplot2.svg
/usr/lib64/R/library/vdiffr/tests/testthat/_snaps/expect-doppelganger/page-error1.svg
/usr/lib64/R/library/vdiffr/tests/testthat/_snaps/expect-doppelganger/page-error2.svg
/usr/lib64/R/library/vdiffr/tests/testthat/_snaps/foo/expect-doppelganger/variant.svg
/usr/lib64/R/library/vdiffr/tests/testthat/_snaps/ggplot/some-other-title.svg
/usr/lib64/R/library/vdiffr/tests/testthat/_snaps/ggplot/some-title.svg
/usr/lib64/R/library/vdiffr/tests/testthat/helper-mock.R
/usr/lib64/R/library/vdiffr/tests/testthat/helper-vdiffr.R
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/DESCRIPTION
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/tests/figs/base-doppelganger-with-symbol.svg
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/tests/figs/deps.txt
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/tests/figs/ggplot/some-other-title.svg
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/tests/figs/ggplot/some-title.svg
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/tests/figs/myplot.svg
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/tests/figs/myplot2.svg
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/tests/figs/orphaned1.svg
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/tests/figs/passed-plots/grid-doppelganger.svg
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/tests/figs/path2/orphaned2.svg
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/tests/testthat.R
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/tests/testthat/_snaps/failed/myplot.svg
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/tests/testthat/_snaps/ggplot/some-other-title.svg
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/tests/testthat/_snaps/ggplot/some-title.svg
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/tests/testthat/_snaps/new/alt1.svg
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/tests/testthat/_snaps/new/alt2.svg
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/tests/testthat/_snaps/new/context1.svg
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/tests/testthat/_snaps/new/context2.svg
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/tests/testthat/_snaps/new/new1.svg
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/tests/testthat/_snaps/new/new2.svg
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/tests/testthat/_snaps/passed/base-doppelganger-with-symbol.svg
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/tests/testthat/_snaps/passed/grid-doppelganger.svg
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/tests/testthat/_snaps/passed/myplot.svg
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/tests/testthat/_snaps/passed/myplot2.svg
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/tests/testthat/test-failed.R
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/tests/testthat/test-ggplot.R
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/tests/testthat/test-new.R
/usr/lib64/R/library/vdiffr/tests/testthat/mock-pkg/tests/testthat/test-passed.R
/usr/lib64/R/library/vdiffr/tests/testthat/test-expect-doppelganger.R
/usr/lib64/R/library/vdiffr/tests/testthat/test-ggplot.R
/usr/lib64/R/library/vdiffr/tests/testthat/test-log.R
/usr/lib64/R/library/vdiffr/tests/testthat/test-snapshot/_snaps/snapshot/error-resets-snapshots.svg
/usr/lib64/R/library/vdiffr/tests/testthat/test-snapshot/_snaps/snapshot/skip-resets-snapshots.svg
/usr/lib64/R/library/vdiffr/tests/testthat/test-snapshot/test-snapshot.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/vdiffr/libs/vdiffr.so
/V4/usr/lib64/R/library/vdiffr/libs/vdiffr.so
/usr/lib64/R/library/vdiffr/libs/vdiffr.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-vdiffr/0318f6c080dce561fe3e8896ba4b6f2cee4b0f3d
