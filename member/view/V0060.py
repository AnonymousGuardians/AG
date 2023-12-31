from django.shortcuts import render, redirect
from django.views import View

from campaign.models import CampaignInquiry, CampaignInquiryAnswer, CampaignParticipant
from funding.models import FundingInquiry, FundingInquiryAnswer, Funding
from donation.models import DonationInquiry, DonationInquiryAnswer
from member.models import Inquiry, InquiryAnswer
from django.http import JsonResponse
import json


# Create your views here.
# inquiry_type
# 0-답변대기
# 1-답변완료

class InquiryList(View):

    def get(self, request, *args, **kwargs):
        member_id = request.session['member_id']
        campaignList = CampaignInquiry.objects.filter(member_id=member_id,campaign_inquiry_status=1) 
        fundingList = FundingInquiry.objects.filter(member_id=member_id,fundinginquiry_status=1)
        donationList = DonationInquiry.objects.filter(member_id=member_id,donation_inquiry_status=1)
        inquiryList = Inquiry.objects.filter(member_id=member_id,inquiry_status=1)
        

        dataList = {}
        #type
        # 0 - 캠페인
        # 1 - 펀딩
        # 2 - 기부
        # 3 - AG
        cnt = 0
        for key in campaignList:
            answer = CampaignInquiryAnswer.objects.filter(campaign_inquiry_id=key.id)
            answer_status = 0
            answer_create_date, member_name, answer_con = None, None, None
            if answer:
                answer_status = 1
                answer_con = answer[0].campaign_inquiry_answer_content
                answer_create_date = answer[0].create_date.strftime('%Y-%m-%d')
                member_name = answer[0].member.member_name

            data={
                'type':0,
                'inquiry_id':key.id,
                'status':answer_status,
                'content':key.campaign_inquiry_content,
                'answer':answer_con,
                'date':key.create_date.strftime('%Y-%m-%d'),
                'answer_date':answer_create_date,
                'answer_member':member_name
            }

            dataList[cnt] = data
            cnt = cnt + 1

        for key in fundingList:
            answer = FundingInquiryAnswer.objects.filter(funding_inquiry_id=key.id)
            answer_status = 0
            answer_create_date, member_name, answer_con = None, None, None
            if answer:
                answer_status = 1
                answer_con = answer[0].funding_inquiry_answer_content
                answer_create_date = answer[0].create_date.strftime('%Y-%m-%d')
                member_name = answer[0].member.member_name

            data={
                'type':1,
                'inquiry_id':key.id,
                'status':answer_status,
                'content':key.funding_inquiry_content,
                'answer':answer_con,
                'date':key.create_date.strftime('%Y-%m-%d'),
                'answer_date':answer_create_date,
                'answer_member':member_name
            }

            dataList[cnt] = data
            cnt = cnt + 1  


        for key in donationList:
            answer = DonationInquiryAnswer.objects.filter(donation_inquiry_id=key.id)
            answer_status = 0
            answer_create_date, member_name, answer_con = None, None, None
            if answer:
                answer_status = 1
                answer_con = answer[0].donation_inquiry_answer_content
                answer_create_date = answer[0].create_date.strftime('%Y-%m-%d')
                member_name = answer[0].member.member_name

            data={
                'type':2,
                'inquiry_id':key.id,
                'status':answer_status,
                'content':key.donation_inquiry_content,
                'answer':answer_con,
                'date':key.create_date.strftime('%Y-%m-%d'),
                'answer_date':answer_create_date,
                'answer_member':member_name
            }

            dataList[cnt] = data
            cnt = cnt + 1  

        for key in inquiryList:
            answer = InquiryAnswer.objects.filter(inquiry_id=key.id)
            answer_status = 0
            answer_create_date, member_name, answer_con = None, None, None
            if answer:
                answer_status = 1
                answer_con = answer[0].inquiry_answer_content
                answer_create_date = answer[0].create_date.strftime('%Y-%m-%d')
                member_name = answer[0].member.member_name

            data={
                'type':3,
                'inquiry_id':key.id,
                'status':answer_status,
                'content':key.inquiry_content,
                'answer':answer_con,
                'date':key.create_date.strftime('%Y-%m-%d'),
                'answer_date':answer_create_date,
                'answer_member':member_name
            }

            dataList[cnt] = data
            cnt = cnt + 1      


        sorted_data = dict(sorted(dataList.items(), key=lambda item: item[1]['date'], reverse=True))




        joinList = CampaignParticipant.objects.filter(member_id=member_id,campaign_participant_role='L') 
        
        cnt2 = 0
        dataList2 = {}
        for key in joinList:
            data = {}
            campaign = CampaignInquiry.objects.filter(campaign_id=key.campaign_id,campaign_inquiry_status=1)
            funding = None
            if Funding.objects.filter(campaign_id=key.campaign_id):
                funding = FundingInquiry.objects.filter(funding_id=Funding.objects.filter(campaign_id=key.campaign_id)[0].id,fundinginquiry_status=1)

            if campaign:
                answer = CampaignInquiryAnswer.objects.filter(campaign_inquiry_id=campaign[0].id)
                answer_status = 0
                answer_create_date, member_name, answer_con = None, None, None
                if answer:
                    answer_status = 1
                    answer_con = answer[0].campaign_inquiry_answer_content
                    answer_create_date = answer[0].create_date.strftime('%Y-%m-%d')
                    member_name = answer[0].member.member_name
                data={
                    'type':0,
                    'inquiry_id':key.campaign_id,
                    'status':answer_status,
                    'content':campaign[0].campaign_inquiry_content,
                    'answer':answer_con,
                    'date':campaign[0].create_date.strftime('%Y-%m-%d'),
                    'answer_date':answer_create_date,
                    'answer_member':member_name
                }
                
                dataList2[cnt2] = data
                cnt2 = cnt2 + 1    

            if funding:
                answer = FundingInquiryAnswer.objects.filter(funding_inquiry_id=funding[0].id)
                answer_status = 0
                answer_create_date, member_name, answer_con = None, None, None
                if answer:
                    answer_status = 1
                    answer_con = answer[0].funding_inquiry_answer_content
                    answer_create_date = answer[0].create_date.strftime('%Y-%m-%d')
                    member_name = answer[0].member.member_name
                data={
                    'type':1,
                    'inquiry_id':key.campaign_id,
                    'status':answer_status,
                    'content':funding[0].funding_inquiry_content,
                    'answer':answer_con,
                    'date':funding[0].create_date.strftime('%Y-%m-%d'),
                    'answer_date':answer_create_date,
                    'answer_member':member_name
                }    
                
                dataList2[cnt2] = data
                cnt2 = cnt2 + 1  

        sorted_data2 = dict(sorted(dataList2.items(), key=lambda item: item[1]['date'], reverse=True))
          

        return render(request, 'mypage/mypage__007/_T007.html',{'context':sorted_data,'context2':sorted_data2})

    def post(self, request, *args, **kwargs):     
        
        try:
            data = json.loads(request.body)
            # answer = CityHeader.objects.get(city_name=data['city_header_name'])
            # city_detail = CityDetail.objects.get(city_detail_name=data['city_detail_name'])
            
            # user = Member.objects.get(id=data['member_id'])
            # user.city_header_id = city_header.id
            # user.city_detail_id = city_detail.id
            # user.save()

        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        return JsonResponse({'result': 'OK'}, status=200)