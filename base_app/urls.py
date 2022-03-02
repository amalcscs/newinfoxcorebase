from . import views
from django.urls import re_path


urlpatterns=[ 
    re_path(r'^$',views.login,name='login'),
    re_path(r'^Admlogout$',views.Admlogout,name='Admlogout'),
    re_path(r'^Mnlogout$',views.Mnlogout,name='Mnlogout'),

#***************************anandu***********************************
    re_path(r'^MAN_profiledash$', views.MAN_profiledash,name='MAN_profiledash'),
    re_path(r'^MAN_index$', views.MAN_index, name='MAN_index'),
    re_path(r'^MAN_employees$', views.MAN_employees, name='MAN_employees'),
    re_path(r'^MAN_python/(?P<id>\d+)$', views.MAN_python, name='MAN_python'),
    re_path(r'^MAN_projectman/(?P<id>\d+)/(?:(?P<did>\d+))?', views.MAN_projectman, name='MAN_projectman'),
    re_path(r'^MAN_proname/(?P<id>\d+)$', views.MAN_proname, name='MAN_proname'),
    re_path(r'^MAN_proinvolve/(?P<id>\d+)$', views.MAN_proinvolve, name='MAN_proinvolve'),
    re_path(r'^MAN_promanatten/(?P<id>\d+)/$', views.MAN_promanatten, name='MAN_promanatten'),
    re_path(r'^MAN_promanattendsort/(?P<id>\d+)/$', views.MAN_promanattendsort, name='MAN_promanattensort'),

    re_path(r'^BRadmin_profiledash$', views.BRadmin_profiledash,name='BRadmin_profiledash'),
    re_path(r'^BRadmin_index$', views.BRadmin_index, name='BRadmin_index'),
    re_path(r'^BRadmin_employees$', views.BRadmin_employees, name='BRadmin_employees'),
    re_path(r'^BRadmin_python/(?P<id>\d+)$', views.BRadmin_python, name='BRadmin_python'),
    re_path(r'^BRadmin_projectman/(?P<id>\d+)/(?:(?P<did>\d+))?', views.BRadmin_projectman, name='BRadmin_projectman'),
    re_path(r'^BRadmin_proname/(?P<id>\d+)$', views.BRadmin_proname, name='BRadmin_proname'),
    re_path(r'^BRadmin_proinvolve/(?P<id>\d+)$', views.BRadmin_proinvolve, name='BRadmin_proinvolve'),
    re_path(r'^BRadmin_promanatten/(?P<id>\d+)/$', views.BRadmin_promanatten, name='BRadmin_promanatten'),
    re_path(r'^BRadmin_promanattendsort/(?P<id>\d+)/$', views.BRadmin_promanattendsort, name='BRadmin_promanattensort'),


    #********************praveen********************************
    re_path(r'^BRadmin_trainerstable$', views.BRadmin_trainerstable,name='BRadmin_trainerstable'),
    re_path(r'^BRadmin_Training/(?P<id>\d+)$', views.BRadmin_Training,name='BRadmin_Training'),
    re_path(r'^BRadmin_trainingteam1/(?P<id>\d+)$', views.BRadmin_trainingteam1,name='BRadmin_trainingteam1'),
    re_path(r'^BRadmin_traineestable/(?P<id>\d+)$', views.BRadmin_traineestable,name='BRadmin_traineestable'),
    re_path(r'^BRadmin_trainingprofile/(?P<id>\d+)$', views.BRadmin_trainingprofile,name='BRadmin_trainingprofile'),
    re_path(r'^BRadmin_completedtasktable/(?P<id>\d+)$', views.BRadmin_completedtasktable,name='BRadmin_completedtasktable'),
    re_path(r'^BRadmin_topictable/(?P<id>\d+)$', views.BRadmin_topictable,name='BRadmin_topictable'),

    re_path(r'^MAN_trainerstable/$', views.MAN_trainerstable,name='MAN_trainerstable'),
    re_path(r'^MAN_Training/(?P<id>\d+)/$', views.MAN_Training,name='MAN_Training'),
    re_path(r'^MAN_trainingteam1/(?P<id>\d+)/$', views.MAN_trainingteam1,name='MAN_trainingteam1'),
    re_path(r'^MAN_traineestable/(?P<id>\d+)/$', views.MAN_traineestable,name='MAN_traineestable'),
    re_path(r'^MAN_trainingprofile/(?P<id>\d+)/$', views.MAN_trainingprofile,name='MAN_trainingprofile'),
    re_path(r'^MAN_completedtasktable/(?P<id>\d+)/$', views.MAN_completedtasktable,name='MAN_completedtasktable'),
    re_path(r'^MAN_topictable/(?P<id>\d+)/$', views.MAN_topictable,name='MAN_topictable'),



#************************  anwar   *********************************************

    re_path(r'^BRadmin_View_Trainers/(?P<id>\d+)/(?:(?P<did>\d+))?', views.BRadmin_View_Trainers, name='BRadmin_View_Trainers'),
    re_path(r'^BRadmin_View_Trainerprofile/(?P<id>\d+)$', views.BRadmin_View_Trainerprofile, name='BRadmin_View_Trainerprofile'),

    re_path(r'^BRadmin_View_Currenttraineesoftrainer/(?P<id>\d+)/$', views.BRadmin_View_Currenttraineesoftrainer, name='BRadmin_View_Currenttraineesoftrainer'),

    re_path(r'^BRadmin_View_Previoustraineesoftrainer/(?P<id>\d+)/$', views.BRadmin_View_Previoustraineesoftrainer, name='BRadmin_View_Previoustraineesoftrainer'),

    re_path(r'^BRadmin_View_Currenttraineeprofile/(?P<id>\d+)$', views.BRadmin_View_Currenttraineeprofile, name='BRadmin_View_Currenttraineeprofile'),

    re_path(r'^BRadmin_View_Currenttraineetasks/(?P<id>\d+)$', views.BRadmin_View_Currenttraineetasks, name='BRadmin_View_Currenttraineetasks'),

    re_path(r'^BRadmin_View_Currenttraineeattendance/(?P<id>\d+)$', views.BRadmin_View_Currenttraineeattendance, name='BRadmin_View_Currenttraineeattendance'),

    re_path(r'^BRadmin_View_Previoustraineesoftrainer$', views.BRadmin_View_Previoustraineesoftrainer, name='BRadmin_View_Previoustraineesoftrainer'),

    re_path(r'^BRadmin_View_Previoustraineeprofile/(?P<id>\d+)$', views.BRadmin_View_Previoustraineeprofile, name='BRadmin_View_Previoustraineeprofile'),

    re_path(r'^BRadmin_View_Previoustraineetasks/(?P<id>\d+)$', views.BRadmin_View_Previoustraineetasks, name='BRadmin_View_Previoustraineetasks'),

    re_path(r'^BRadmin_View_Previoustraineeattendance/(?P<id>\d+)$', views.BRadmin_View_Previoustraineeattendance, name='BRadmin_View_Previoustraineeattendance'),

    re_path(r'^BRadmin_View_Trainerattendance/(?P<id>\d+)$', views.BRadmin_View_Trainerattendance, name='BRadmin_View_Trainerattendance'),

    re_path(r'^BRadmin_ViewTrainerattendancesort/(?P<id>\d+)/$', views.BRadmin_ViewTrainerattendancesort, name='BRadmin_ViewTrainerattendancesort'),

    re_path(r'^BRadmin_ViewCurrenttraineeattendancesort/(?P<id>\d+)/$', views.BRadmin_ViewCurrenttraineeattendancesort, name='BRadmin_ViewCurrenttraineeattendancesort'),

    re_path(r'^BRadmin_ViewPrevioustraineeattendancesort/(?P<id>\d+)/$', views.BRadmin_ViewPrevioustraineeattendancesort, name='BRadmin_ViewPrevioustraineeattendancesort'),

    re_path(r'^BRadmin_attendance$',views.admin_page1,name='admin_page1'),
    re_path(r'^BRadmin_attendanceshow$',views.admin_page3,name='admin_page3'),

    re_path(r'^admin_desi$',views.admin_desi,name='admin_desi'),
    re_path(r'^admin_emp$',views.admin_emp,name='admin_emp'),



    re_path(r'^MAN_View_Trainers/(?P<id>\d+)/(?:(?P<did>\d+))?', views.MAN_View_Trainers, name='MAN_View_Trainers'),
    re_path(r'^MAN_View_Trainerprofile/(?P<id>\d+)$', views.MAN_View_Trainerprofile, name='MAN_View_Trainerprofile'),


    re_path(r'^MAN_View_Currenttraineesoftrainer/(?P<id>\d+)/$', views.MAN_View_Currenttraineesoftrainer, name='MAN_View_Currenttraineesoftrainer'),

    re_path(r'^MAN_View_Previoustraineesoftrainer/(?P<id>\d+)/$', views.MAN_View_Previoustraineesoftrainer, name='MAN_View_Previoustraineesoftrainer'),

    re_path(r'^MAN_View_Currenttraineeprofile/(?P<id>\d+)$', views.MAN_View_Currenttraineeprofile, name='MAN_View_Currenttraineeprofile'),

    re_path(r'^MAN_View_Currenttraineetasks/(?P<id>\d+)$', views.MAN_View_Currenttraineetasks, name='MAN_View_Currenttraineetasks'),

    re_path(r'^MAN_View_Currenttraineeattendance/(?P<id>\d+)$', views.MAN_View_Currenttraineeattendance, name='MAN_View_Currenttraineeattendance'),

    re_path(r'^MAN_View_Previoustraineesoftrainer$', views.MAN_View_Previoustraineesoftrainer, name='MAN_View_Previoustraineesoftrainer'),

    re_path(r'^MAN_View_Previoustraineeprofile/(?P<id>\d+)$', views.MAN_View_Previoustraineeprofile, name='MAN_View_Previoustraineeprofile'),

    re_path(r'^MAN_View_Previoustraineetasks/(?P<id>\d+)$', views.MAN_View_Previoustraineetasks, name='MAN_View_Previoustraineetasks'),

    re_path(r'^MAN_View_Previoustraineeattendance/(?P<id>\d+)$', views.MAN_View_Previoustraineeattendance, name='MAN_View_Previoustraineeattendance'),

    re_path(r'^MAN_View_Trainerattendance/(?P<id>\d+)$', views.MAN_View_Trainerattendance, name='MAN_View_Trainerattendance'),


    re_path(r'^MAN_ViewTrainerattendancesort/(?P<id>\d+)/$', views.MAN_ViewTrainerattendancesort, name='MAN_ViewTrainerattendancesort'),

    re_path(r'^MAN_ViewCurrenttraineeattendancesort/(?P<id>\d+)/$', views.MAN_ViewCurrenttraineeattendancesort, name='MAN_ViewCurrenttraineeattendancesort'),

    re_path(r'^MAN_ViewPrevioustraineeattendancesort/(?P<id>\d+)/$', views.MAN_ViewPrevioustraineeattendancesort, name='MAN_ViewPrevioustraineeattendancesort'),

    re_path(r'^MAN_dev_attendance$',views.MAN_dev_attendance,name='MAN_dev_attendance'),

    re_path(r'^MAN_attendance$',views.man_page1,name='man_page1'),
    re_path(r'^MAN_attendanceshow$',views.man_page3,name='man_page3'),

    re_path(r'^man_desi$',views.man_desi,name='man_desi'),
    re_path(r'^man_emp$',views.man_emp,name='man_emp'),
#************************  anwar end  *********************************************



# current projects-sharon -admin mod

    # re_path(r'^BRadmin_profiledash$', views.BRadmin_profiledash,name='BRadmin_profiledash'),
    re_path(r'^BRadmin_dept$', views.BRadmin_dept, name='BRadmin_dept'),
    re_path(r'^BRadmin_pythons$', views.BRadmin_pythons, name='BRadmin_pythons'),
    re_path(r'^BRadmin_projects/(?P<id>\d+)/$', views.BRadmin_projects, name='BRadmin_projects'),
    re_path(r'^BRadmin_proj_list/(?P<id>\d+)/$', views.BRadmin_proj_list, name='BRadmin_proj_list'),
    re_path(r'^BRadmin_proj_det/(?P<id>\d+)/$', views.BRadmin_proj_det, name='BRadmin_proj_det'),
    re_path(r'^BRadmin_proj_mngrs/(?P<id>\d+)/$', views.BRadmin_proj_mngrs, name='BRadmin_proj_mngrs'),
    re_path(r'^BRadmin_proj_mangrs1/(?P<id>\d+)/$', views.BRadmin_proj_mangrs1, name='BRadmin_proj_mangrs1'),
    re_path(r'^BRadmin_proj_mangrs2/(?P<id>\d+)/$', views.BRadmin_proj_mangrs2, name='BRadmin_proj_mangrs2'),  
    re_path(r'^BRadmin_daily_report/(?P<id>\d+)/$', views.BRadmin_daily_report, name='BRadmin_daily_report'),
    re_path(r'^BRadmin_developers/(?P<id>\d+)/$', views.BRadmin_developers, name='BRadmin_developers'),


# completed projects-subeeesh -admin mod

    re_path(r'^BRadmin_proj_cmpltd_new/(?P<id>\d+)/$', views.BRadmin_proj_cmpltd_new, name='BRadmin_proj_cmpltd_new'),
    re_path(r'^BRadmin_cmpltd_proj_det_new/(?P<id>\d+)/$', views.BRadmin_cmpltd_proj_det_new, name='BRadmin_cmpltd_proj_det_new'),
    re_path(r'^BRadmin_proj_mngrs_new/(?P<id>\d+)/$', views.BRadmin_proj_mngrs_new, name='BRadmin_proj_mngrs_new'),
    re_path(r'^BRadmin_proj_mangrs1_new/(?P<id>\d+)/$', views.BRadmin_proj_mangrs1_new, name='BRadmin_proj_mangrs1_new'),
    re_path(r'^BRadmin_proj_mangrs2_new/(?P<id>\d+)/$', views.BRadmin_proj_mangrs2_new, name='BRadmin_proj_mangrs2_new'),
    re_path(r'^BRadmin_developers_new/(?P<id>\d+)/$', views.BRadmin_developers_new, name='BRadmin_developers_new'),
    re_path(r'^BRadmin_daily_report_new/(?P<id>\d+)/$', views.BRadmin_daily_report_new, name='BRadmin_daily_report_new'),

# current projects-sharon -admin mod

    # re_path(r'^MAN_profiledash$', views.MAN_profiledash,name='MAN_profiledash'),
    re_path(r'^MAN_dept$', views.MAN_dept, name='MAN_dept'),
    re_path(r'^MAN_pythons$', views.MAN_pythons, name='MAN_pythons'),
    re_path(r'^MAN_projects/(?P<id>\d+)/$', views.MAN_projects, name='MAN_projects'),
    re_path(r'^MAN_proj_list/(?P<id>\d+)/$', views.MAN_proj_list, name='MAN_proj_list'),
    re_path(r'^MAN_proj_det/(?P<id>\d+)/$', views.MAN_proj_det, name='MAN_proj_det'),
    re_path(r'^MAN_proj_mngrs/(?P<id>\d+)/$', views.MAN_proj_mngrs, name='MAN_proj_mngrs'),
    re_path(r'^MAN_proj_mangrs1/(?P<id>\d+)/$', views.MAN_proj_mangrs1, name='MAN_proj_mangrs1'),
    re_path(r'^MAN_proj_mangrs2/(?P<id>\d+)/$', views.MAN_proj_mangrs2, name='MAN_proj_mangrs2'),  
    re_path(r'^MAN_daily_report/(?P<id>\d+)/$', views.MAN_daily_report, name='MAN_daily_report'),
    re_path(r'^MAN_developers/(?P<id>\d+)/$', views.MAN_developers, name='MAN_developers'),


# completed projects-subeeesh -man mod

    re_path(r'^MAN_proj_cmpltd_new/(?P<id>\d+)/$', views.MAN_proj_cmpltd_new, name='MAN_proj_cmpltd_new'),
    re_path(r'^MAN_cmpltd_proj_det_new/(?P<id>\d+)/$', views.MAN_cmpltd_proj_det_new, name='MAN_cmpltd_proj_det_new'),
    re_path(r'^MAN_proj_mngrs_new/(?P<id>\d+)/$', views.MAN_proj_mngrs_new, name='MAN_proj_mngrs_new'),
    re_path(r'^MAN_proj_mangrs1_new/(?P<id>\d+)/$', views.MAN_proj_mangrs1_new, name='MAN_proj_mangrs1_new'),
    re_path(r'^MAN_proj_mangrs2_new/(?P<id>\d+)/$', views.MAN_proj_mangrs2_new, name='MAN_proj_mangrs2_new'),
    re_path(r'^MAN_developers_new/(?P<id>\d+)/$', views.MAN_developers_new, name='MAN_developers_new'),
    re_path(r'^MAN_daily_report_new/(?P<id>\d+)/$', views.MAN_daily_report_new, name='MAN_daily_report_new'),


########## end ##########

#reported issue- akhil-admin mod

    re_path(r'^BRadmin_Reportedissue_department$', views.BRadmin_Reportedissue_department, name='BRadmin_Reportedissue_department'),
    re_path(r'^BRadmin_Reportedissue/(?P<id>\d+)$', views.BRadmin_Reportedissue, name='BRadmin_Reportedissue'),
    re_path(r'^BRadmin_ReportedissueShow/(?P<id>\d+)$', views.BRadmin_ReportedissueShow, name='BRadmin_ReportedissueShow'),
    re_path(r'^BRadmin_ReportedissueShow1/(?P<id>\d+)$', views.BRadmin_ReportedissueShow1, name='BRadmin_ReportedissueShow1'),

#reported issue- akhil-man mod

    re_path(r'^MAN_Reportedissue_department$', views.MAN_Reportedissue_department, name='MAN_Reportedissue_department'),
    re_path(r'^MAN_Reportedissue/(?P<id>\d+)$', views.MAN_Reportedissue, name='MAN_Reportedissue'),
    re_path(r'^MAN_ReportedissueShow/(?P<id>\d+)$', views.MAN_ReportedissueShow, name='MAN_ReportedissueShow'),
    re_path(r'^MAN_ReportedissueShow1/(?P<id>\d+)$', views.MAN_ReportedissueShow1, name='MAN_ReportedissueShow1'),

########## end ##########

 #task section-nimisha- man mod   

    re_path(r'^MAN_tasks$', views.MAN_tasks, name='MAN_tasks'),
    re_path(r'MAN_givetask$', views.MAN_givetask, name='MAN_givetask'),
    re_path(r'^MAN_currenttasks$', views.MAN_currenttasks, name='MAN_currenttasks'),
    re_path(r'^MAN_previoustasks$', views.MAN_previoustasks, name='MAN_previoustasks'),
    re_path(r'MAN_taskemployee$', views.MAN_taskemployee, name='MAN_taskemployee'),
    re_path(r'MAN_taskdesignation$', views.MAN_taskdesignation, name='MAN_taskdesignation'),


 #task section-nimisha- admin mod   

    re_path(r'^BRadmin_tasks$', views.BRadmin_tasks, name='BRadmin_tasks'),
    re_path(r'BRadmin_givetask$', views.BRadmin_givetask, name='BRadmin_givetask'),
    re_path(r'^BRadmin_currenttasks$', views.BRadmin_currenttasks, name='BRadmin_currenttasks'),
    re_path(r'^BRadmin_previoustasks$', views.BRadmin_previoustasks, name='BRadmin_previoustasks'),
    re_path(r'BRadmin_taskemployee$', views.BRadmin_taskemployee, name='BRadmin_taskemployee'),
    re_path(r'BRadmin_taskdesignation$', views.BRadmin_taskdesignation, name='BRadmin_taskdesignation'),   


########## end ##########


#upcoming projects -safdhar -admin mod

    re_path(r'^BRadmin_upcoming$', views.BRadmin_upcoming, name='BRadmin_upcoming'),
    re_path(r'^BRadmin_viewprojectform$', views.BRadmin_viewprojectform, name='BRadmin_viewprojectform'),
    re_path(r'^BRadmin_acceptedprojects$', views.BRadmin_acceptedprojects, name='BRadmin_acceptedprojects'),
    re_path(r'^BRadmin_rejected$', views.BRadmin_rejected, name='BRadmin_rejected'),
    re_path(r'^BRadmin_createproject$', views.BRadmin_createproject, name='BRadmin_createproject'),
    re_path(r'^BRadmin_upcomingpro$', views.BRadmin_upcomingpro, name='BRadmin_upcomingpro'),
    re_path(r'^BRadmin_seradmintraineedesi1$', views.BRadmin_seradmintraineedesi1, name='BRadmin_seradmintraineedesi1'),
    re_path(r'^BRadmin_seradmindesig$', views.BRadmin_seradmindesig, name='BRadmin_seradmindesig'),
    re_path(r'^BRadmin_selectproject$', views.BRadmin_selectproject, name='BRadmin_selectproject'),


#upcoming projects -safdhar -man mod

    re_path(r'^MAN_upcoming$', views.MAN_upcoming, name='MAN_upcoming'),
    re_path(r'^MAN_viewprojectform$', views.MAN_viewprojectform, name='MAN_viewprojectform'),
    re_path(r'^MAN_acceptedprojects$', views.MAN_acceptedprojects, name='MAN_acceptedprojects'),
    re_path(r'^MAN_rejected$', views.MAN_rejected, name='MAN_rejected'),
    re_path(r'^MAN_upcomingprojectsview$', views.MAN_upcomingprojectsview, name='MAN_upcomingprojectsview'),
    re_path(r'^MAN_createproject$', views.MAN_createproject, name='MAN_createproject'),
    re_path(r'^MAN_seradmintraineedesi1$', views.MAN_seradmintraineedesi1, name='MAN_seradmintraineedesi1'),
    re_path(r'^MAN_seradmindesig$', views.MAN_seradmindesig, name='MAN_seradmindesig'),
    re_path(r'^MAN_selectproject$', views.MAN_selectproject, name='MAN_selectproject'),


#********************meenu************************
    re_path(r'^man_newdept$',views.man_newdept,name='man_newdept'),
    re_path(r'^man_dept$',views.man_dept,name='man_dept'),
    re_path(r'^man_add_deptsave$',views.man_add_deptsave,name='man_add_deptsave'),
    re_path(r'^man_delete/(?P<id>\d+)$', views.man_delete,name='man_delete'),

    re_path(r'^newdept$',views.newdept,name='newdept'),
    re_path(r'^add_dept$',views.add_dept,name='add_dept'),
    re_path(r'^add_deptsave$',views.add_deptsave,name='add_deptsave'),
    re_path(r'^delete/(?P<id>\d+)$', views.delete,name='delete'),

########## end ##########

]