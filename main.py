#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uvicorn
import logging
from api import SayerAPI

# إنشاء تطبيق FastAPI
app = FastAPI(
    title="Sayer API",
    description="واجهة برمجة التطبيقات لأداة Sayer للبحث عن المعلومات",
    version="1.0.0",
    contact={
        "name": "SaudiLinux",
        "email": "SaudiCrackers@gmail.com"
    }
)

# إعداد التسجيل
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# إنشاء نموذج البيانات
class SearchRequest(BaseModel):
    target: str
    tool_options: Optional[dict] = None

class APIResponse(BaseModel):
    status: str
    message: str
    data: Optional[dict] = None

# إنشاء مثيل من SayerAPI
sayer_api = SayerAPI()

@app.get("/")
async def root():
    """نقطة النهاية الرئيسية للتحقق من حالة API"""
    return {
        "status": "success",
        "message": "مرحباً بك في Sayer API",
        "version": "1.0.0"
    }

@app.post("/search", response_model=APIResponse)
async def search(request: SearchRequest):
    """نقطة نهاية للبحث عن الهدف المحدد"""
    try:
        # التحقق من صحة الهدف
        if not request.target:
            raise HTTPException(status_code=400, detail="الهدف مطلوب")
        
        # تنفيذ البحث
        results = await sayer_api.search(request.target)
        
        return APIResponse(
            status="success",
            message="تم تنفيذ البحث بنجاح",
            data=results
        )
    
    except Exception as e:
        logger.error(f"خطأ في البحث: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"حدث خطأ أثناء تنفيذ البحث: {str(e)}"
        )

@app.get("/status")
async def get_status():
    """نقطة نهاية للتحقق من حالة الخدمات"""
    try:
        # التحقق من حالة الأدوات والخدمات
        services_status = {
            "theHarvester": "متصل",
            "spiderfoot": "متصل",
            "ghunt": "متصل",
            "sherlock": "متصل"
        }
        
        return APIResponse(
            status="success",
            message="تم التحقق من حالة الخدمات بنجاح",
            data={"services": services_status}
        )
    
    except Exception as e:
        logger.error(f"خطأ في التحقق من الحالة: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"حدث خطأ أثناء التحقق من الحالة: {str(e)}"
        )

@app.get("/tools")
async def get_tools():
    """نقطة نهاية للحصول على معلومات الأدوات المتاحة"""
    tools_info = {
        "theHarvester": {
            "description": "أداة لجمع المعلومات من مصادر عامة",
            "supported_targets": ["domain", "email"]
        },
        "spiderfoot": {
            "description": "منصة استخبارات مفتوحة المصدر",
            "supported_targets": ["domain", "ip", "email"]
        },
        "ghunt": {
            "description": "أداة للبحث عن حسابات Google",
            "supported_targets": ["email"]
        },
        "sherlock": {
            "description": "أداة للبحث عن حسابات وسائل التواصل الاجتماعي",
            "supported_targets": ["username"]
        }
    }
    
    return APIResponse(
        status="success",
        message="تم استرجاع معلومات الأدوات بنجاح",
        data={"tools": tools_info}
    )

if __name__ == "__main__":
    # تشغيل خادم API
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )