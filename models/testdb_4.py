# Người dùng
user = {
    'user_id': '',  # id user: SV_01, GV_01, ADM_01, GĐ_01
    # chức vụ của user: admin, student, manager, teacher
    'role_user': {
        'admin': '',
        'manager': '',
        'teacher': '',
        'student': ''
    },
    'full_name': '',  # tên đầy đủ: vd Nguyễn Bá Hải Bánh
    'avatar': '',  # Hình ảnh đại diện
    'user_name': '',  # tài khoản
    'email': '',  # có thể login bằng email
    'password': '',  # mật khẩu
    'profile': {
        'academic_level': '',  # trình độ học vấn giáo viên tại thời điềm cấp bằng cho sinh viên khi mã NFT
        'identify_image': '',  # ảnh cấp bằng dùng cho sinh, giáo viên xác nhận giáo viên
        'signature': '',  # ảnh chữ kí (path)
        'study_time': '',  # thời gian học tập (chỉ dành cho student)
        'gender': '',  # giới tính
        'date_of_birth': '',  # ngày sinh
        'address': '',  # địa chỉ
        'city': '',  # Thành phố
        'province': '',  # Tỉnh
        'phone': '',  # số điện thoại
        'graduate_active': '',
        # trạng thái ENUM {'not-graduate':'Chưa tốt nghiệp', 'graduated':'Đã tốt nghiệp', 'reserve':'Bảo lưu' }
    },
    'created_time': '',
    'updated_time': '',
    # chứng minh thư, căn cước công dân
    'citizen_identity_card': {
        'no': '',
        'date_of_issue': '',
        'date_of_exprity': '',
    },
    # thông tin trường học
    'school': [{
        'school_id': '',  # tên trường
        'school_name': '',  # tên trường
        'level_count': '',
        # cấp trường : vd tiểu học-1, trung học cơ sở-2, trung học phổ thông-3, đại học-4, học viện-4
        'school_type': '',  # loại trường : vd tiểu học, trung học cơ sở, vv
        'is_active': '',  # trạng thái
        'created_time': '',
        'updated_time': '',
        # Khoa : Công nghệ thông tin, Quản trị kinh doanh
        'department': {
            'department_name': '',
            # nghành học : Kỹ thuật phần mền, Hệ thống thông tin, Trí tuệ nhân tọa AI,An Toàn thông tin
            'major': [{
                'major_name': '',
                # Lớp : vd Công nghệ phần mềm 1, công nghệ thông tin 2
                'class': [{
                    'class_name': '',
                    'start_year': '',
                    'graduate_year': ''
                },
                    {
                        'class_name': '',
                        'start-year': '',
                        'graduate-year': ''
                    }]
            },
                {
                    'major_name': '',
                    # Lớp : vd Quản trị kinh doanh 1, Quản trị kinh doanh 2
                    'class': [{
                        'class_name': '',
                        'start_year': '',
                        'graduate_year': ''
                    },
                        {
                            'class_name': '',
                            'start-year': '',
                            'graduate_year': ''  # k54
                        }
                    ],
                }
            ]
        }}]
}

## Trường học
school = {
    'school_name': '',  # tên trường
    'level_count': '',  # cấp trường : vd tiểu học-1, trung học cơ sở-2, trung học phổ thông-3, đại học-4, học viện-4
    'school_type': '',  # loại trường : vd tiểu học, trung học cơ sở, vv
    'is_active': '',  # trạng thái
    'created_time': '',
    'updated_time': '',
    # Khoa : Công nghệ thông tin, Quản trị kinh doanh
    'department': {
        'department_name': '',
        # nghành học : Kỹ thuật phần mền, Hệ thống thông tin, Trí tuệ nhân tọa AI,An Toàn thông tin
        'major': [{
            'major_name': '',
            # Lớp : vd Công nghệ phần mềm 1, công nghệ thông tin 2
            'class': [{
                'class_name': '',
                'start-year': '',
                'graduate-year': ''  # k54
            }],
        }]
    }
}

## Bằng
diplomas = {
    'user_id': '',  # id sinh viên
    'graduate_info': [{
        'vi': {
            # cộng hòa xã hội chủ nghĩa việt nam
            'tile': '',  # độc lập - tự do - hạnh phúc
            'school': {
                'school_name': '',  # tên trường
                'level_count': '',
                # cấp trường : vd tiểu học-1, trung học cơ sở-2, trung học phổ thông-3, đại học-4, học viện-4
                'school_type': '',  # loại trường : vd tiểu học, trung học cơ sở, vv
                # Khoa : Công nghệ thông tin, Quản trị kinh doanh
                'department': {
                    'department_name': '',
                    # nghành học : Kỹ thuật phần mền, Hệ thống thông tin, Trí tuệ nhân tọa AI,An Toàn thông tin
                    'major': {
                        'major_name': ''
                    }
                }
            },
            'training_system': '',  # hệ đào tạo : vd cử nhân, kĩ sư, cao đẳng, trung cấp
            'student': {
                'full_name': '',  # tên đầy đủ: vd Nguyễn Bá Hải
                'date_of_birth': '',  # ngày sinh
                'province': ''  # Tỉnh
            }
        },
        'en': {
            # cộng hòa xã hội chủ nghĩa việt nam
            'tile': '',  # độc lập - tự do - hạnh phúc
            'school': {
                'school_name': '',  # tên trường
                'level_count': '',
                # cấp trường : vd tiểu học-1, trung học cơ sở-2, trung học phổ thông-3, đại học-4, học viện-4
                'school_type': '',  # loại trường : vd tiểu học, trung học cơ sở, vv
                # Khoa : Công nghệ thông tin, Quản trị kinh doanh
                'department': {
                    'department_name': '',
                    # nghành học : Kỹ thuật phần mền, Hệ thống thông tin, Trí tuệ nhân tọa AI,An Toàn thông tin
                    'major': {
                        'major_name': ''
                    }
                }
            },
            'training_system': '',  # hệ đào tạo : vd cử nhân, kĩ sư, cao đẳng, trung cấp
            # thông tin user
            'student': {
                'full_name': '',  # tên đầy đủ: vd Nguyễn Bá Hải
                'date_of_birth': '',  # ngày sinh
                'province': ''  # Tỉnh
            }
        }
    }],
    'academic_ability': '',  # học lực
    'awarded_place': '',  # nơi cấp bằng
    'awarded_date': '',  # ngày cấp bằng
    'degree_awarder': '',  # thông tin người cấp
    'id_graduate_certification': '',  # số hiệu bằng, mã bằng
    'graduate_certification_date': '',  # Ngày quyết định cấp bằng
    'signature_header_master': '',  # chữ kí hiệu
    'signature_student': '',  # chữ kí sinh viên
    'diploma_image': '',  # ảnh bằng
    'transcript': [{
        'transcript_academic': {
            'transcript_academic_id': '',  # Mã môn học
            'transcript_academic_name': '',  # Tên môn học
            'transcript_academic_number': ''  # Số học tín chỉ, học phần
        },
        'point': '',  # Điểm
        'teacher': {  # giáp viên xác nhận học phần
            'user_id': '',  # id user: SV_01, GV_01, ADM_01, GĐ_01
            # chức vụ của user: admin, student, manager, teacher
            'role_user': {
                'admin': '',
                'manager': '',
                'teacher': '',
                'student': ''
            },
            'full_name': '',  # tên đầy đủ: vd Nguyễn Bá Hải
            'profile': {
                'academic_level': '',  # trình độ học vấn giáo viên tại thời điềm cấp bằng cho sinh viên khi mã NFT
                'identify_image': '',  # ảnh cấp bằng dùng cho sinh, giáo viên xác nhận giáo viên
                'signature': '',  # ảnh chữ kí giáo viên
            }
        }
    },
        {
            'transcript_academic': {
                'transcript_academic_id': '',  # Mã môn học
                'transcript_academic_name': '',  # Tên môn học
                'transcript_academic_number': ''  # Số học tín chỉ, học phần
            },
            'point': '',  # Điểm
            'teacher': {  # giáp viên xác nhận học phần
                'user_id': '',  # id user: SV_01, GV_01, ADM_01, GĐ_01
                # chức vụ của user: admin, student, manager, teacher
                'role_user': {
                    'admin': '',
                    'manager': '',
                    'teacher': '',
                    'student': ''
                },
                'full_name': '',  # tên đầy đủ: vd Nguyễn Bá Hải
                'profile': {
                    'academic_level': '',  # trình độ học vấn giáo viên tại thời điềm cấp bằng cho sinh viên khi mã NFT
                    'identify_image': '',  # ảnh cấp bằng dùng cho sinh, giáo viên xác nhận giáo viên
                    'signature': '',  # ảnh chữ kí giáo viên
                }
            }
        }
    ]
}

# ## Resumes
# 'transcript_academic': {
#     'transcript_academic_id': '',  # Mã môn học
#     'transcript_academic_name': '',  # Tên môn học
#     'transcript_academic_number': ''  # Số học tín chỉ, học phần
# }
#
# ## Kiến trúc enum
# 'academic_ability': {
#     'excellent': 'Giỏi',
#     'good': 'Khá'
#             'average': 'Trung bình'
# }
#
# ## department - Khoa
# 'department': {
#     'department_id': '',  # Mã khoa
#     'department_name': ''
# }
#
# ## major - Nghành học
# 'major': {
#     'major_id': '',  # Mã nghành
#     'major_name': ''
# }
#
# ## role user
# 'role_user': {
#     'admin': ' Quản trị',
#     'manager': 'Quản lý',
#     'teacher': 'Giáo viên',
#     'student': 'Sinh viên'
# }

# api_key :jrvRtmOndgsJ.drmZT/uS3M8X5uH479Fh8q3ighNAXs