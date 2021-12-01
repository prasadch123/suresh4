from django.shortcuts import render
from .models import LearnAI,LearnAI_2,LearnAI_3,LearnAI_4,LearnAI_5,LearnAI_6
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError

def index(request):
    if request.method=="POST":
        text=request.POST.get('text')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        whatsup=request.POST.get('whatsup')
        occupation=request.POST.get('occupation')
        Looking=request.POST.get('Looking')
        if Looking=="1":
            department1=request.POST.get('department1')
            department2=request.POST.get('department2')
            department3=request.POST.get('department3')
            department4=request.POST.get('department4')
            department5=request.POST.get('department5')
            department6=request.POST.get('department6')


            request.session['text']=text
            request.session['email']=email
            request.session['phone']=phone
            request.session['whatsup']=whatsup
            request.session['occupation']=occupation
            request.session['Looking']=Looking
            request.session['department1']=department1
            request.session['department2']=department2
            request.session['department3']=department3
            request.session['department4']=department4
            request.session['department5']=department5
            request.session['department6']=department6

            subject = 'Student Details'
            dummy = 'Name: '+str(text)+'\nEmail: '+str(email)+'\nPhone Number: '+str(phone)+'\nWhatsup Number:'+str(whatsup)+'\nOccupation :'+str(occupation)+'\nLooking :'+str(Looking)+'\nMode :'+str(department1)+'\nCourse :'+str(department2)+'\nJoining :'+str(department3)+'\nWeek :'+str(department4)+'\nTiming :'+str(department5)+'\nAdditional_course :'+str(department6)
            try:

                send_mail(subject, dummy, 'learnai356@gmail.com', ['learnai356@gmail.com'])
                data=LearnAI(
                name=text,
                email=email,
                mobile=phone,
                whatsup=whatsup,
                occupation=occupation,
                Looking=Looking,
                department1=department1,
                department2=department2,
                department3=department3,
                department4=department4,
                department5=department5,
                department6=department6
                )
                data.save()
                return render(request,'index.html')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        
        

        elif Looking=="2":
            project=request.POST.get('project')
            type1=request.POST.get('type1')
            projects=request.POST.get('projects')
            student=request.POST.get('student')
            


            request.session['text']=text
            request.session['email']=email
            request.session['phone']=phone
            request.session['whatsup']=whatsup
            request.session['occupation']=occupation
            request.session['Looking']=Looking
            request.session['project']=project
            request.session['type1']=type1
            request.session['projects']=projects
            request.session['student']=student
            

            subject = 'Student Details'
            dummy = 'Name: '+str(text)+'\nEmail: '+str(email)+'\nPhone Number: '+str(phone)+'\nWhatsup Number:'+str(whatsup)+'\nOccupation :'+str(occupation)+'\nLooking :'+str(Looking)+'\nEducation :'+str(project)+'\nType of Project :'+str(type1)+'\nStudent Projects :'+str(projects)+'\nAdditional_project :'+str(student)
            try:

                send_mail(subject, dummy, 'learnai356@gmail.com', ['learnai356@gmail.com'])
                data1=LearnAI_2(
                name=text,
                email=email,
                mobile=phone,
                whatsup=whatsup,
                occupation=occupation,
                Looking=Looking,
                project=project,
                type1=type1,
                projects=projects,
                student=student,
                
                )
                data1.save()
                return render(request,'index.html')

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        
        

        elif Looking=="3":
            intern1=request.POST.get('intern1')
            internship=request.POST.get('internship')
            time=request.POST.get('time')
            
            


            request.session['text']=text
            request.session['email']=email
            request.session['phone']=phone
            request.session['whatsup']=whatsup
            request.session['occupation']=occupation
            request.session['Looking']=Looking
            request.session['intern1']=intern1
            request.session['internship']=internship
            request.session['time']=time
            
            

            subject = 'Student Details'
            dummy = 'Name: '+str(text)+'\nEmail: '+str(email)+'\nPhone Number: '+str(phone)+'\nWhatsup Number:'+str(whatsup)+'\nOccupation :'+str(occupation)+'\nLooking :'+str(Looking)+'\nType of Internship :'+str(intern1)+'\nTime Duration :'+str(internship)+'\nAdditional Internship :'+str(time)
            try:

                send_mail(subject, dummy, 'learnai356@gmail.com', ['learnai356@gmail.com'])
                data1=LearnAI_3(
                name=text,
                email=email,
                mobile=phone,
                whatsup=whatsup,
                occupation=occupation,
                Looking=Looking,
                intern1=intern1,
                internship=internship,
                time=time,
                
                )
                data1.save()
                return render(request,'index.html')

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        
            

        elif Looking=="4":
            job=request.POST.get('job')
            job1=request.POST.get('job1')
            
            


            request.session['text']=text
            request.session['email']=email
            request.session['phone']=phone
            request.session['whatsup']=whatsup
            request.session['occupation']=occupation
            request.session['Looking']=Looking
            request.session['job']=job
            request.session['job1']=job1
            
            

            subject = 'Student Details'
            dummy = 'Name: '+str(text)+'\nEmail: '+str(email)+'\nPhone Number: '+str(phone)+'\nWhatsup Number:'+str(whatsup)+'\nOccupation :'+str(occupation)+'\nLooking :'+str(Looking)+'\nJob Support :'+str(job)+'\nAdditional Job Support :'+str(job1)
            try:

                send_mail(subject, dummy, 'learnai356@gmail.com', ['learnai356@gmail.com'])
                data1=LearnAI_4(
                name=text,
                email=email,
                mobile=phone,
                whatsup=whatsup,
                occupation=occupation,
                Looking=Looking,
                job=job,
                job1=job1,
                
                
                )
                data1.save()
                return render(request,'index.html')

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        
            
        elif Looking=="5":
            visa=request.POST.get('visa')
            visa1=request.POST.get('visa1')
            country=request.POST.get('country')
            
            
            request.session['text']=text
            request.session['email']=email
            request.session['phone']=phone
            request.session['whatsup']=whatsup
            request.session['occupation']=occupation
            request.session['Looking']=Looking
            request.session['visa']=visa
            request.session['visa1']=visa1
            request.session['country']=country

            subject = 'Student Details'
            dummy = 'Name: '+str(text)+'\nEmail: '+str(email)+'\nPhone Number: '+str(phone)+'\nWhatsup Number:'+str(whatsup)+'\nOccupation :'+str(occupation)+'\nLooking :'+str(Looking)+'\nvisa process :'+str(visa)+'\nCountry :'+str(visa1)+'\nAdditional visa process :'+str(country)
            try:

                send_mail(subject, dummy, 'learnai356@gmail.com', ['learnai356@gmail.com'])

                data1=LearnAI_5(
                name=text,
                email=email,
                mobile=phone,
                whatsup=whatsup,
                occupation=occupation,
                Looking=Looking,
                visa=visa,
                visa1=visa1,
                country=country
                
                )
                data1.save()
                
                return render(request,'index.html')

            except BadHeaderError:
                return HttpResponse('Invalid header found.')

        else:
            job_assi=request.POST.get('job_assi')
            job_assi1=request.POST.get('job_assi1')
            
            request.session['text']=text
            request.session['email']=email
            request.session['phone']=phone
            request.session['whatsup']=whatsup
            request.session['occupation']=occupation
            request.session['Looking']=Looking
            request.session['job_assi']=job_assi
            request.session['job_assi1']=job_assi1
            
            subject = 'Student Details'
            dummy = 'Name: '+str(text)+'\nEmail: '+str(email)+'\nPhone Number: '+str(phone)+'\nWhatsup Number:'+str(whatsup)+'\nOccupation :'+str(occupation)+'\nLooking :'+str(Looking)+'\nJob_assitance :'+str(job_assi)+'\nAdditional Job_assitance :'+str(job_assi1)
            try:

                send_mail(subject, dummy, 'learnai356@gmail.com', ['learnai356@gmail.com'])

                data1=LearnAI_6(
                name=text,
                email=email,
                mobile=phone,
                whatsup=whatsup,
                occupation=occupation,
                Looking=Looking,
                job_assi=job_assi,
                job_assi1=job_assi1,
                
                
                )
                data1.save()
                
                return render(request,'index.html')

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        
    else:
        return render(request,'index.html')