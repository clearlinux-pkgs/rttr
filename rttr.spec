#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rttr
Version  : 0.9.6
Release  : 5
URL      : https://github.com/rttrorg/rttr/archive/v0.9.6.tar.gz
Source0  : https://github.com/rttrorg/rttr/archive/v0.9.6.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rttr-data = %{version}-%{release}
Requires: rttr-lib = %{version}-%{release}
Requires: rttr-license = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : glibc-dev
Patch1: werror-is-for-werrorists.patch
Patch2: Change_OWNER_READ_permission_in_cmake_files.patch

%description
[![Version](https://badge.fury.io/gh/rttrorg%2Frttr.svg)](https://github.com/rttrorg/rttr/releases/latest)
[![Travis status](https://travis-ci.org/rttrorg/rttr.svg?branch=master)](https://travis-ci.org/rttrorg/rttr)
[![Appveyor status](https://ci.appveyor.com/api/projects/status/github/rttrorg/rttr?svg=true&branch=master)](https://ci.appveyor.com/project/acki-m/rttr)
[![Coverage Status](https://coveralls.io/repos/rttrorg/rttr/badge.svg?branch=master&service=github)](https://coveralls.io/github/rttrorg/rttr)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/783/badge)](https://bestpractices.coreinfrastructure.org/projects/783)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9821799170644782ac8d7885d393e686)](https://www.codacy.com/app/acki-m/rttr?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=rttrorg/rttr&amp;utm_campaign=Badge_Grade)
[![Documentation](https://img.shields.io/badge/docs-latest-blue.svg)](http://www.rttr.org/doc/master/classes.html)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/rttrorg/rttr/master/LICENSE.txt)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=JQ65KGGCSUZMS)

%package data
Summary: data components for the rttr package.
Group: Data

%description data
data components for the rttr package.


%package dev
Summary: dev components for the rttr package.
Group: Development
Requires: rttr-lib = %{version}-%{release}
Requires: rttr-data = %{version}-%{release}
Provides: rttr-devel = %{version}-%{release}
Requires: rttr = %{version}-%{release}

%description dev
dev components for the rttr package.


%package lib
Summary: lib components for the rttr package.
Group: Libraries
Requires: rttr-data = %{version}-%{release}
Requires: rttr-license = %{version}-%{release}

%description lib
lib components for the rttr package.


%package license
Summary: license components for the rttr package.
Group: Default

%description license
license components for the rttr package.


%prep
%setup -q -n rttr-0.9.6
cd %{_builddir}/rttr-0.9.6
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1632200648
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DBUILD_UNIT_TESTS=OFF
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1632200648
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rttr
cp %{_builddir}/rttr-0.9.6/LICENSE.txt %{buildroot}/usr/share/package-licenses/rttr/bdd981ce0fa4af170de8ca29b2521f88fd073187
cp %{_builddir}/rttr-0.9.6/doc/md_pages/license.md %{buildroot}/usr/share/package-licenses/rttr/94305339cac78b76f2e3e0933c7286fc79ab5a06
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/doc/index.html
/usr/doc/rttr-0-9-6/access__levels_8h.html
/usr/doc/rttr-0-9-6/access__levels_8h_source.html
/usr/doc/rttr-0-9-6/annotated.html
/usr/doc/rttr-0-9-6/argument_8h.html
/usr/doc/rttr-0-9-6/argument_8h_source.html
/usr/doc/rttr-0-9-6/array__range_8h.html
/usr/doc/rttr-0-9-6/array__range_8h_source.html
/usr/doc/rttr-0-9-6/associative__mapper_8h.html
/usr/doc/rttr-0-9-6/associative__mapper_8h_source.html
/usr/doc/rttr-0-9-6/bc_s.png
/usr/doc/rttr-0-9-6/bdwn.png
/usr/doc/rttr-0-9-6/bootstrap/css/bootstrap.min.css
/usr/doc/rttr-0-9-6/bootstrap/js/bootstrap.min.js
/usr/doc/rttr-0-9-6/building__install_8md.html
/usr/doc/rttr-0-9-6/building_install_page.html
/usr/doc/rttr-0-9-6/classes.html
/usr/doc/rttr-0-9-6/classrttr_1_1argument-members.html
/usr/doc/rttr-0-9-6/classrttr_1_1argument.html
/usr/doc/rttr-0-9-6/classrttr_1_1array__range-members.html
/usr/doc/rttr-0-9-6/classrttr_1_1array__range.html
/usr/doc/rttr-0-9-6/classrttr_1_1basic__string__view-members.html
/usr/doc/rttr-0-9-6/classrttr_1_1basic__string__view.html
/usr/doc/rttr-0-9-6/classrttr_1_1constructor-members.html
/usr/doc/rttr-0-9-6/classrttr_1_1constructor.html
/usr/doc/rttr-0-9-6/classrttr_1_1destructor-members.html
/usr/doc/rttr-0-9-6/classrttr_1_1destructor.html
/usr/doc/rttr-0-9-6/classrttr_1_1enum__flags-members.html
/usr/doc/rttr-0-9-6/classrttr_1_1enum__flags.html
/usr/doc/rttr-0-9-6/classrttr_1_1enumeration-members.html
/usr/doc/rttr-0-9-6/classrttr_1_1enumeration.html
/usr/doc/rttr-0-9-6/classrttr_1_1instance-members.html
/usr/doc/rttr-0-9-6/classrttr_1_1instance.html
/usr/doc/rttr-0-9-6/classrttr_1_1library-members.html
/usr/doc/rttr-0-9-6/classrttr_1_1library.html
/usr/doc/rttr-0-9-6/classrttr_1_1method-members.html
/usr/doc/rttr-0-9-6/classrttr_1_1method.html
/usr/doc/rttr-0-9-6/classrttr_1_1parameter__info-members.html
/usr/doc/rttr-0-9-6/classrttr_1_1parameter__info.html
/usr/doc/rttr-0-9-6/classrttr_1_1property-members.html
/usr/doc/rttr-0-9-6/classrttr_1_1property.html
/usr/doc/rttr-0-9-6/classrttr_1_1registration-members.html
/usr/doc/rttr-0-9-6/classrttr_1_1registration.html
/usr/doc/rttr-0-9-6/classrttr_1_1registration_1_1bind-members.html
/usr/doc/rttr-0-9-6/classrttr_1_1registration_1_1bind.html
/usr/doc/rttr-0-9-6/classrttr_1_1registration_1_1bind.png
/usr/doc/rttr-0-9-6/classrttr_1_1registration_1_1class__-members.html
/usr/doc/rttr-0-9-6/classrttr_1_1registration_1_1class__.html
/usr/doc/rttr-0-9-6/classrttr_1_1type-members.html
/usr/doc/rttr-0-9-6/classrttr_1_1type.html
/usr/doc/rttr-0-9-6/classrttr_1_1variant-members.html
/usr/doc/rttr-0-9-6/classrttr_1_1variant.html
/usr/doc/rttr-0-9-6/classrttr_1_1variant__associative__view-members.html
/usr/doc/rttr-0-9-6/classrttr_1_1variant__associative__view.html
/usr/doc/rttr-0-9-6/classrttr_1_1variant__associative__view_1_1const__iterator-members.html
/usr/doc/rttr-0-9-6/classrttr_1_1variant__associative__view_1_1const__iterator.html
/usr/doc/rttr-0-9-6/classrttr_1_1variant__sequential__view-members.html
/usr/doc/rttr-0-9-6/classrttr_1_1variant__sequential__view.html
/usr/doc/rttr-0-9-6/classrttr_1_1variant__sequential__view_1_1const__iterator-members.html
/usr/doc/rttr-0-9-6/classrttr_1_1variant__sequential__view_1_1const__iterator.html
/usr/doc/rttr-0-9-6/closed.png
/usr/doc/rttr-0-9-6/constructor_8h.html
/usr/doc/rttr-0-9-6/constructor_8h_source.html
/usr/doc/rttr-0-9-6/custom-bootstrap.css
/usr/doc/rttr-0-9-6/custom-doxygen.css
/usr/doc/rttr-0-9-6/default__arguments_8md.html
/usr/doc/rttr-0-9-6/default_arguments_page.html
/usr/doc/rttr-0-9-6/destructor_8h.html
/usr/doc/rttr-0-9-6/destructor_8h_source.html
/usr/doc/rttr-0-9-6/dir_9950a74130ece602e761643b15cf9815.html
/usr/doc/rttr-0-9-6/dir_e68e8157741866f444e17edd764ebbae.html
/usr/doc/rttr-0-9-6/dir_f5cf7324fde9d3df625992c311710e35.html
/usr/doc/rttr-0-9-6/doc.png
/usr/doc/rttr-0-9-6/doxy-boot.js
/usr/doc/rttr-0-9-6/doxygen.css
/usr/doc/rttr-0-9-6/doxygen.svg
/usr/doc/rttr-0-9-6/dynsections.js
/usr/doc/rttr-0-9-6/enum__flags_8h.html
/usr/doc/rttr-0-9-6/enum__flags_8h_source.html
/usr/doc/rttr-0-9-6/enumeration_8h.html
/usr/doc/rttr-0-9-6/enumeration_8h_source.html
/usr/doc/rttr-0-9-6/favicon.ico
/usr/doc/rttr-0-9-6/filter__item_8h.html
/usr/doc/rttr-0-9-6/filter__item_8h_source.html
/usr/doc/rttr-0-9-6/five__minute__tutorial_8md.html
/usr/doc/rttr-0-9-6/five_minute_tutorial_page.html
/usr/doc/rttr-0-9-6/folderclosed.png
/usr/doc/rttr-0-9-6/folderopen.png
/usr/doc/rttr-0-9-6/fonts/ptsans_regular_macroman/PTS55F-demo.html
/usr/doc/rttr-0-9-6/fonts/ptsans_regular_macroman/PTS55F-webfont.eot
/usr/doc/rttr-0-9-6/fonts/ptsans_regular_macroman/PTS55F-webfont.svg
/usr/doc/rttr-0-9-6/fonts/ptsans_regular_macroman/PTS55F-webfont.ttf
/usr/doc/rttr-0-9-6/fonts/ptsans_regular_macroman/PTS55F-webfont.woff
/usr/doc/rttr-0-9-6/fonts/ptsans_regular_macroman/specimen_files/PTS55F-cleartype.png
/usr/doc/rttr-0-9-6/fonts/ptsans_regular_macroman/specimen_files/easytabs.js
/usr/doc/rttr-0-9-6/fonts/ptsans_regular_macroman/specimen_files/grid_12-825-55-15.css
/usr/doc/rttr-0-9-6/fonts/ptsans_regular_macroman/specimen_files/specimen_stylesheet.css
/usr/doc/rttr-0-9-6/fonts/ptsans_regular_macroman/stylesheet.css
/usr/doc/rttr-0-9-6/fonts/source_code_pro_regular/SourceCodePro-Regular-webfont.eot
/usr/doc/rttr-0-9-6/fonts/source_code_pro_regular/SourceCodePro-Regular-webfont.svg
/usr/doc/rttr-0-9-6/fonts/source_code_pro_regular/SourceCodePro-Regular-webfont.ttf
/usr/doc/rttr-0-9-6/fonts/source_code_pro_regular/SourceCodePro-Regular-webfont.woff
/usr/doc/rttr-0-9-6/fonts/source_code_pro_regular/demo.html
/usr/doc/rttr-0-9-6/fonts/source_code_pro_regular/stylesheet.css
/usr/doc/rttr-0-9-6/functions.html
/usr/doc/rttr-0-9-6/functions_b.html
/usr/doc/rttr-0-9-6/functions_c.html
/usr/doc/rttr-0-9-6/functions_d.html
/usr/doc/rttr-0-9-6/functions_e.html
/usr/doc/rttr-0-9-6/functions_f.html
/usr/doc/rttr-0-9-6/functions_func.html
/usr/doc/rttr-0-9-6/functions_func_b.html
/usr/doc/rttr-0-9-6/functions_func_c.html
/usr/doc/rttr-0-9-6/functions_func_d.html
/usr/doc/rttr-0-9-6/functions_func_e.html
/usr/doc/rttr-0-9-6/functions_func_f.html
/usr/doc/rttr-0-9-6/functions_func_g.html
/usr/doc/rttr-0-9-6/functions_func_h.html
/usr/doc/rttr-0-9-6/functions_func_i.html
/usr/doc/rttr-0-9-6/functions_func_l.html
/usr/doc/rttr-0-9-6/functions_func_m.html
/usr/doc/rttr-0-9-6/functions_func_n.html
/usr/doc/rttr-0-9-6/functions_func_o.html
/usr/doc/rttr-0-9-6/functions_func_p.html
/usr/doc/rttr-0-9-6/functions_func_r.html
/usr/doc/rttr-0-9-6/functions_func_s.html
/usr/doc/rttr-0-9-6/functions_func_t.html
/usr/doc/rttr-0-9-6/functions_func_u.html
/usr/doc/rttr-0-9-6/functions_func_v.html
/usr/doc/rttr-0-9-6/functions_func_~.html
/usr/doc/rttr-0-9-6/functions_g.html
/usr/doc/rttr-0-9-6/functions_h.html
/usr/doc/rttr-0-9-6/functions_i.html
/usr/doc/rttr-0-9-6/functions_k.html
/usr/doc/rttr-0-9-6/functions_l.html
/usr/doc/rttr-0-9-6/functions_m.html
/usr/doc/rttr-0-9-6/functions_n.html
/usr/doc/rttr-0-9-6/functions_o.html
/usr/doc/rttr-0-9-6/functions_p.html
/usr/doc/rttr-0-9-6/functions_r.html
/usr/doc/rttr-0-9-6/functions_rela.html
/usr/doc/rttr-0-9-6/functions_s.html
/usr/doc/rttr-0-9-6/functions_t.html
/usr/doc/rttr-0-9-6/functions_type.html
/usr/doc/rttr-0-9-6/functions_u.html
/usr/doc/rttr-0-9-6/functions_v.html
/usr/doc/rttr-0-9-6/functions_vars.html
/usr/doc/rttr-0-9-6/functions_w.html
/usr/doc/rttr-0-9-6/functions_z.html
/usr/doc/rttr-0-9-6/functions_~.html
/usr/doc/rttr-0-9-6/hierarchy.html
/usr/doc/rttr-0-9-6/index.html
/usr/doc/rttr-0-9-6/instance_8h.html
/usr/doc/rttr-0-9-6/instance_8h_source.html
/usr/doc/rttr-0-9-6/jquery.js
/usr/doc/rttr-0-9-6/jquery.min.js
/usr/doc/rttr-0-9-6/library_8h.html
/usr/doc/rttr-0-9-6/library_8h_source.html
/usr/doc/rttr-0-9-6/license_8md.html
/usr/doc/rttr-0-9-6/license_page.html
/usr/doc/rttr-0-9-6/main__page_8md.html
/usr/doc/rttr-0-9-6/menu.js
/usr/doc/rttr-0-9-6/menudata.js
/usr/doc/rttr-0-9-6/meta__data_8md.html
/usr/doc/rttr-0-9-6/method_8h.html
/usr/doc/rttr-0-9-6/method_8h_source.html
/usr/doc/rttr-0-9-6/namespacemembers.html
/usr/doc/rttr-0-9-6/namespacemembers_enum.html
/usr/doc/rttr-0-9-6/namespacemembers_func.html
/usr/doc/rttr-0-9-6/namespacemembers_type.html
/usr/doc/rttr-0-9-6/namespacerttr.html
/usr/doc/rttr-0-9-6/nav_f.png
/usr/doc/rttr-0-9-6/nav_g.png
/usr/doc/rttr-0-9-6/nav_h.png
/usr/doc/rttr-0-9-6/open.png
/usr/doc/rttr-0-9-6/pages.html
/usr/doc/rttr-0-9-6/parameter__info_8h.html
/usr/doc/rttr-0-9-6/parameter__info_8h_source.html
/usr/doc/rttr-0-9-6/parameter__names_8md.html
/usr/doc/rttr-0-9-6/parameter_names_page.html
/usr/doc/rttr-0-9-6/policies_8md.html
/usr/doc/rttr-0-9-6/policy_8h.html
/usr/doc/rttr-0-9-6/policy_8h_source.html
/usr/doc/rttr-0-9-6/property_8h.html
/usr/doc/rttr-0-9-6/property_8h_source.html
/usr/doc/rttr-0-9-6/query__info__type_8md.html
/usr/doc/rttr-0-9-6/register__class__hierachy_8md.html
/usr/doc/rttr-0-9-6/register__classes_8md.html
/usr/doc/rttr-0-9-6/register__enums_8md.html
/usr/doc/rttr-0-9-6/register__hello__world_8md.html
/usr/doc/rttr-0-9-6/register__methods_8md.html
/usr/doc/rttr-0-9-6/register__plugins_8md.html
/usr/doc/rttr-0-9-6/register__properties_8md.html
/usr/doc/rttr-0-9-6/register_classes_page.html
/usr/doc/rttr-0-9-6/register_enums_page.html
/usr/doc/rttr-0-9-6/register_hello_world_page.html
/usr/doc/rttr-0-9-6/register_metadata_page.html
/usr/doc/rttr-0-9-6/register_methods_page.html
/usr/doc/rttr-0-9-6/register_plugins.html
/usr/doc/rttr-0-9-6/register_policies_page.html
/usr/doc/rttr-0-9-6/register_properties_page.html
/usr/doc/rttr-0-9-6/register_variant_page.html
/usr/doc/rttr-0-9-6/registration_8h.html
/usr/doc/rttr-0-9-6/registration_8h_source.html
/usr/doc/rttr-0-9-6/registration__friend_8h.html
/usr/doc/rttr-0-9-6/registration__friend_8h_source.html
/usr/doc/rttr-0-9-6/rttr__cast_8h.html
/usr/doc/rttr-0-9-6/rttr__cast_8h_source.html
/usr/doc/rttr-0-9-6/rttr__enable_8h.html
/usr/doc/rttr-0-9-6/rttr__enable_8h_source.html
/usr/doc/rttr-0-9-6/rttr_type_class_hierachy_page.html
/usr/doc/rttr-0-9-6/rttr_type_get_page.html
/usr/doc/rttr-0-9-6/rttr_type_info_page.html
/usr/doc/rttr-0-9-6/rttr_type_rttr_cast_page.html
/usr/doc/rttr-0-9-6/sequential__mapper_8h.html
/usr/doc/rttr-0-9-6/sequential__mapper_8h_source.html
/usr/doc/rttr-0-9-6/splitbar.png
/usr/doc/rttr-0-9-6/string__view_8h.html
/usr/doc/rttr-0-9-6/string__view_8h_source.html
/usr/doc/rttr-0-9-6/structrttr_1_1associative__container__mapper-members.html
/usr/doc/rttr-0-9-6/structrttr_1_1associative__container__mapper.html
/usr/doc/rttr-0-9-6/structrttr_1_1policy.html
/usr/doc/rttr-0-9-6/structrttr_1_1policy_1_1ctor-members.html
/usr/doc/rttr-0-9-6/structrttr_1_1policy_1_1ctor.html
/usr/doc/rttr-0-9-6/structrttr_1_1policy_1_1meth-members.html
/usr/doc/rttr-0-9-6/structrttr_1_1policy_1_1meth.html
/usr/doc/rttr-0-9-6/structrttr_1_1policy_1_1prop-members.html
/usr/doc/rttr-0-9-6/structrttr_1_1policy_1_1prop.html
/usr/doc/rttr-0-9-6/structrttr_1_1sequential__container__mapper-members.html
/usr/doc/rttr-0-9-6/structrttr_1_1sequential__container__mapper.html
/usr/doc/rttr-0-9-6/structrttr_1_1wrapper__mapper-members.html
/usr/doc/rttr-0-9-6/structrttr_1_1wrapper__mapper.html
/usr/doc/rttr-0-9-6/sync_off.png
/usr/doc/rttr-0-9-6/sync_on.png
/usr/doc/rttr-0-9-6/tab_a.png
/usr/doc/rttr-0-9-6/tab_b.png
/usr/doc/rttr-0-9-6/tab_h.png
/usr/doc/rttr-0-9-6/tab_s.png
/usr/doc/rttr-0-9-6/tabs.css
/usr/doc/rttr-0-9-6/tutorial_8md.html
/usr/doc/rttr-0-9-6/tutorial_page.html
/usr/doc/rttr-0-9-6/type_8h.html
/usr/doc/rttr-0-9-6/type_8h_source.html
/usr/doc/rttr-0-9-6/using__rttr__cast_8md.html
/usr/doc/rttr-0-9-6/using__rttr__type_8md.html
/usr/doc/rttr-0-9-6/variant_8h.html
/usr/doc/rttr-0-9-6/variant_8h_source.html
/usr/doc/rttr-0-9-6/variant_8md.html
/usr/doc/rttr-0-9-6/variant__associative__view_8h.html
/usr/doc/rttr-0-9-6/variant__associative__view_8h_source.html
/usr/doc/rttr-0-9-6/variant__sequential__view_8h.html
/usr/doc/rttr-0-9-6/variant__sequential__view_8h_source.html
/usr/doc/rttr-0-9-6/wrapper__mapper_8h.html
/usr/doc/rttr-0-9-6/wrapper__mapper_8h_source.html

%files data
%defattr(-,root,root,-)
/usr/share/rttr/LICENSE.txt
/usr/share/rttr/README.md
/usr/share/rttr/cmake/rttr-config-relwithdebinfo.cmake
/usr/share/rttr/cmake/rttr-config-version.cmake
/usr/share/rttr/cmake/rttr-config.cmake

%files dev
%defattr(-,root,root,-)
/usr/include/rttr/access_levels.h
/usr/include/rttr/argument.h
/usr/include/rttr/array_range.h
/usr/include/rttr/associative_mapper.h
/usr/include/rttr/constructor.h
/usr/include/rttr/destructor.h
/usr/include/rttr/detail/base/core_prerequisites.h
/usr/include/rttr/detail/base/version.h
/usr/include/rttr/detail/comparison/comparable_types.h
/usr/include/rttr/detail/comparison/compare_array_equal.h
/usr/include/rttr/detail/comparison/compare_array_equal_impl.h
/usr/include/rttr/detail/comparison/compare_array_less.h
/usr/include/rttr/detail/comparison/compare_array_less_impl.h
/usr/include/rttr/detail/comparison/compare_equal.h
/usr/include/rttr/detail/comparison/compare_equal_impl.h
/usr/include/rttr/detail/comparison/compare_less.h
/usr/include/rttr/detail/comparison/compare_less_impl.h
/usr/include/rttr/detail/constructor/constructor_invoker.h
/usr/include/rttr/detail/constructor/constructor_wrapper.h
/usr/include/rttr/detail/constructor/constructor_wrapper_base.h
/usr/include/rttr/detail/constructor/constructor_wrapper_defaults.h
/usr/include/rttr/detail/conversion/number_conversion.h
/usr/include/rttr/detail/conversion/std_conversion_functions.h
/usr/include/rttr/detail/default_arguments/default_arguments.h
/usr/include/rttr/detail/default_arguments/invoke_with_defaults.h
/usr/include/rttr/detail/destructor/destructor_wrapper.h
/usr/include/rttr/detail/destructor/destructor_wrapper_base.h
/usr/include/rttr/detail/enumeration/enum_data.h
/usr/include/rttr/detail/enumeration/enumeration_helper.h
/usr/include/rttr/detail/enumeration/enumeration_wrapper.h
/usr/include/rttr/detail/enumeration/enumeration_wrapper_base.h
/usr/include/rttr/detail/filter/filter_item_funcs.h
/usr/include/rttr/detail/impl/argument_impl.h
/usr/include/rttr/detail/impl/array_range_impl.h
/usr/include/rttr/detail/impl/associative_mapper_impl.h
/usr/include/rttr/detail/impl/enum_flags_impl.h
/usr/include/rttr/detail/impl/instance_impl.h
/usr/include/rttr/detail/impl/rttr_cast_impl.h
/usr/include/rttr/detail/impl/sequential_mapper_impl.h
/usr/include/rttr/detail/impl/string_view_impl.h
/usr/include/rttr/detail/impl/wrapper_mapper_impl.h
/usr/include/rttr/detail/metadata/metadata.h
/usr/include/rttr/detail/metadata/metadata_handler.h
/usr/include/rttr/detail/method/method_accessor.h
/usr/include/rttr/detail/method/method_invoker.h
/usr/include/rttr/detail/method/method_wrapper.h
/usr/include/rttr/detail/method/method_wrapper_base.h
/usr/include/rttr/detail/misc/argument_extractor.h
/usr/include/rttr/detail/misc/argument_wrapper.h
/usr/include/rttr/detail/misc/class_item_mapper.h
/usr/include/rttr/detail/misc/data_address_container.h
/usr/include/rttr/detail/misc/flat_map.h
/usr/include/rttr/detail/misc/flat_multimap.h
/usr/include/rttr/detail/misc/function_traits.h
/usr/include/rttr/detail/misc/iterator_wrapper.h
/usr/include/rttr/detail/misc/misc_type_traits.h
/usr/include/rttr/detail/misc/register_wrapper_mapper_conversion.h
/usr/include/rttr/detail/misc/sequential_container_type_traits.h
/usr/include/rttr/detail/misc/std_type_traits.h
/usr/include/rttr/detail/misc/template_type_trait.h
/usr/include/rttr/detail/misc/template_type_trait_impl.h
/usr/include/rttr/detail/misc/utility.h
/usr/include/rttr/detail/parameter_info/parameter_info_wrapper.h
/usr/include/rttr/detail/parameter_info/parameter_info_wrapper_base.h
/usr/include/rttr/detail/parameter_info/parameter_infos.h
/usr/include/rttr/detail/parameter_info/parameter_infos_compare.h
/usr/include/rttr/detail/parameter_info/parameter_names.h
/usr/include/rttr/detail/policies/ctor_policies.h
/usr/include/rttr/detail/policies/meth_policies.h
/usr/include/rttr/detail/policies/prop_policies.h
/usr/include/rttr/detail/property/property_accessor.h
/usr/include/rttr/detail/property/property_wrapper.h
/usr/include/rttr/detail/property/property_wrapper_base.h
/usr/include/rttr/detail/property/property_wrapper_func.h
/usr/include/rttr/detail/property/property_wrapper_member_func.h
/usr/include/rttr/detail/property/property_wrapper_member_object.h
/usr/include/rttr/detail/property/property_wrapper_object.h
/usr/include/rttr/detail/registration/bind_impl.h
/usr/include/rttr/detail/registration/bind_types.h
/usr/include/rttr/detail/registration/register_base_class_from_accessor.h
/usr/include/rttr/detail/registration/registration_executer.h
/usr/include/rttr/detail/registration/registration_impl.h
/usr/include/rttr/detail/registration/registration_manager.h
/usr/include/rttr/detail/registration/registration_state_saver.h
/usr/include/rttr/detail/type/accessor_type.h
/usr/include/rttr/detail/type/base_classes.h
/usr/include/rttr/detail/type/get_create_variant_func.h
/usr/include/rttr/detail/type/get_derived_info_func.h
/usr/include/rttr/detail/type/type_comparator.h
/usr/include/rttr/detail/type/type_converter.h
/usr/include/rttr/detail/type/type_data.h
/usr/include/rttr/detail/type/type_impl.h
/usr/include/rttr/detail/type/type_name.h
/usr/include/rttr/detail/type/type_register.h
/usr/include/rttr/detail/type/type_string_utils.h
/usr/include/rttr/detail/variant/variant_compare.h
/usr/include/rttr/detail/variant/variant_data.h
/usr/include/rttr/detail/variant/variant_data_converter.h
/usr/include/rttr/detail/variant/variant_data_policy.h
/usr/include/rttr/detail/variant/variant_impl.h
/usr/include/rttr/detail/variant_associative_view/variant_associative_view_creator.h
/usr/include/rttr/detail/variant_associative_view/variant_associative_view_creator_impl.h
/usr/include/rttr/detail/variant_associative_view/variant_associative_view_private.h
/usr/include/rttr/detail/variant_sequential_view/variant_sequential_view_creator.h
/usr/include/rttr/detail/variant_sequential_view/variant_sequential_view_creator_impl.h
/usr/include/rttr/detail/variant_sequential_view/variant_sequential_view_private.h
/usr/include/rttr/enum_flags.h
/usr/include/rttr/enumeration.h
/usr/include/rttr/filter_item.h
/usr/include/rttr/instance.h
/usr/include/rttr/library.h
/usr/include/rttr/method.h
/usr/include/rttr/parameter_info.h
/usr/include/rttr/policy.h
/usr/include/rttr/property.h
/usr/include/rttr/registration
/usr/include/rttr/registration.h
/usr/include/rttr/registration_friend
/usr/include/rttr/registration_friend.h
/usr/include/rttr/rttr_cast.h
/usr/include/rttr/rttr_enable.h
/usr/include/rttr/sequential_mapper.h
/usr/include/rttr/string_view.h
/usr/include/rttr/type
/usr/include/rttr/type.h
/usr/include/rttr/variant.h
/usr/include/rttr/variant_associative_view.h
/usr/include/rttr/variant_sequential_view.h
/usr/include/rttr/wrapper_mapper.h
/usr/lib64/librttr_core.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/librttr_core.so.0.9.6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rttr/94305339cac78b76f2e3e0933c7286fc79ab5a06
/usr/share/package-licenses/rttr/bdd981ce0fa4af170de8ca29b2521f88fd073187
